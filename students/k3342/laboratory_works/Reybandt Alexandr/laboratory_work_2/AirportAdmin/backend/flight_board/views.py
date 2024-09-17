from django.db import models
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .service import FlightFilter

from .models import Employee, AirlineCompany, Crew, Airplane, Flight
from .serializers import FlightListSerializer, FlightDetailSerializer, EmployeeSerializer, RegistrationSerializer, \
    AirlineCompanySerializer

from django.shortcuts import render, redirect
from rest_framework.authtoken.models import Token
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer


# class RegistrationAPI(generics.GenericAPIView):
#     serializer_class = RegistrationSerializer
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         return Response({
#             "user": EmployeeSerializer(user, context=self.get_serializer_context()).data,
#             "token": AuthToken.objects.create
#         })

@api_view(['POST', ])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Новый пользователь успешно зарегистрирован!"
            data['username'] = account.username
            data['id'] = account.id
            token = Token.objects.get(user=account).key
            data['token'] = token

        else:
            data = serializer.errors
        return Response(data)


class CustomAuthToken(ObtainAuthToken):
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.id,
        })


class Logout(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


def redirect_flight(request):
    return redirect('flight_list_url', permanent=True)


class FlightListViewSet(viewsets.ModelViewSet):
    """Вывод рейсов"""

    serializer_class = FlightListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = FlightFilter

    def get_queryset(self):
        flights = Flight.objects.all().annotate(
            number_of_seats_available=models.F('number_of_seats') - models.F('number_of_tickets_sold')
        ).annotate(
            duration=models.F('destination_time') - models.F('departure_time')
        )
        return flights

    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return FlightListSerializer
    #     if self.action == 'retrieve':
    #         return FlightDetailSerializer


class FlightDetailViewSet(viewsets.ModelViewSet):
    serializer_class = FlightDetailSerializer
    queryset = Flight.objects.all()

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class EmployeeView(viewsets.ModelViewSet):
    """Вывод информации о пользователе"""

    serializer_class = EmployeeSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # user = self.request.user
        return Employee.objects.filter(pk=self.request.user.id)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class JobApplications(viewsets.ModelViewSet):
    """Вывод информации о поданных заявках"""

    serializer_class = EmployeeSerializer

    def get_queryset(self):
        return Employee.objects.filter(status='На рассмотрении')


class AirlineCompanyView(generics.ListAPIView):
    queryset = AirlineCompany.objects.all()
    serializer_class = AirlineCompanySerializer
