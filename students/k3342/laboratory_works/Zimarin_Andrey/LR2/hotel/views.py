from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from .service import ClientCityFilter, CheckinFilter
from rest_framework.response import Response
from rest_framework import generics, filters
from rest_framework import permissions
from datetime import datetime as dt
from hotel.models import Room, Client, Worker, Cleaning, Checkin, Floor
from hotel.serializers import RoomSer, ClientSer, RoomDetailSer, CheckinSer, CleaningAddSer, AddClientSer, \
                        WorkerSer, CleaningSer, AddCheckinSer, FloorSer, AddWorkerSer, ClientDetailSer, CleaningListSer


class Rooms(APIView):
    """ Вывод всех комнат"""
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        rooms = Room.objects.all()
        rooms = rooms.order_by('room_number')
        serializer = RoomSer(rooms, many=True)
        return Response({'data': serializer.data})


class Clients(APIView):
    """ Вывод всех клиентов"""
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSer(clients, many=True)
        return Response(serializer.data)

    def post(self, request):
        client = AddClientSer(data=request.data)
        if client.is_valid():
            client.save()
            return Response({'status': 'Добавлено'})
        else:
            return Response({'status': 'error'})


class ClientsList(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_class = ClientCityFilter


class RoomDetailsView(APIView):

    def get(self, request, pk):
        rooms = Room.objects.get(room_number=pk)
        serializer = RoomDetailSer(rooms)
        return Response({'data': serializer.data})


class ClientDetailsView(APIView):

    def get(self, request, pk):
        client = Client.objects.get(id=pk)
        serializer = ClientDetailSer(client)
        return Response({'data': serializer.data})


class WorkersView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        workers = Worker.objects.all()
        serializer = WorkerSer(workers, many=True)
        return Response(serializer.data)

    def post(self, request):
        worker = AddWorkerSer(data=request.data)
        if worker.is_valid():
            worker.save()
            return Response({'status': 'Добавлено'})
        else:
            return Response({'status': 'error'})


class DelWorker(APIView):
    """Удаление работника"""
    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request, pk):
        try:
            worker = Worker.objects.get(id=pk)
            worker.delete()
            return Response({'status': 'Удалено'})
        except:
            return Response({'status': 'Ошибка'})


class CleaningTable(APIView):
    """ Расписание уборок одного работника"""
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, pk):
        cleanings = Cleaning.objects.filter(worker=pk)
        serializer = CleaningSer(cleanings, many=True)
        return Response({'data': serializer.data})

    def post(self, request, pk):
        day = request.data.get('day_of_week')
        floor = request.data.get('floor')
        try:
            cleaning = Cleaning.objects.get(worker=pk, day_of_week=day)
            cleaning.floor = Floor.objects.get(id=floor)
            cleaning.save()
            return Response({'status': 'Изменено'})
        except:
            cleaning = CleaningAddSer(data=request.data)
            cleaning.floor = Floor.objects.get(id=floor)
            if cleaning.is_valid():
                cleaning.save()
                return Response({'status': 'Добавлено'})
            else:
                return Response({'status': 'Ошибка'})


class AddCheckin(APIView):
    """ Заселить клиента"""
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        checkins = Checkin.objects.all()
        serializer = CheckinSer(checkins, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        checkin = AddCheckinSer(data=request.data)
        if checkin.is_valid():
            checkin.save()
            return Response({'status': 'Добавлено'})
        else:
            return Response({'status': 'error'})


class FloorsView(APIView):
    def get(self, request):
        floors = Floor.objects.all()
        serializer = FloorSer(floors, many=True)
        return Response({"data": serializer.data})


class CheckinsList(generics.ListAPIView):
    now = dt.now()
    queryset = Checkin.objects.all().order_by('date_in')
    serializer_class = CheckinSer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = CheckinFilter


class CleaningsView(APIView):
    """ Все уборки по дню с указанием комнат"""
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, pk):
        """Pk - день недели"""
        days = {1: 'Пон', 2: 'Вт', 3: 'Ср', 4: 'Чт', 5: 'Пт', 6: 'Сб', 7: 'Вс'}
        cleanings = Cleaning.objects.filter(day_of_week=days[pk])
        serializer = CleaningListSer(cleanings, many=True)
        return Response({'data': serializer.data})
