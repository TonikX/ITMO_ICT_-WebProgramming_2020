from rest_framework.response import Response
from rest_framework import generics
from django.db.models import Q
from datetime import date


# Create your views here.
from .models import *
from .serializers import *


class GetAllPatientView(generics.ListAPIView):
	queryset = Patient.objects.all()
	serializer_class = PatientSerializer


class GetAllPatientCardView(generics.ListAPIView):
	queryset = PatientCard.objects.all()
	serializer_class = PatientCardSerializer


class GetAllDoctorView(generics.ListAPIView):
	queryset = Doctor.objects.all()
	serializer_class = DoctorSerializer


class GetAllAppointmentView(generics.ListAPIView):
	serializer_class = AppointmentSerializer

	def get_queryset(self):
		queryset = Appointment.objects.all()

		params = self.request.query_params

		app_date = params.get('date', None)
		doctor = params.get('doctor', None)

		if app_date and doctor:
			queryset = queryset.filter(Q(doctor__user__username=doctor) & Q(date=app_date))

		return queryset


class GetAllPaymentView(generics.ListAPIView):
	serializer_class = PaymentSerializer

	def get_queryset(self):
		queryset = Payment.objects.all()

		params = self.request.query_params
		
		app_date = params.get('date', None)
		doctor = params.get('doctor', None)
		patient = params.get('patient', None)
		patient_birthdate = params.get('patient_birthdate', None)
		is_paid = params.get('is_paid', None)

		if app_date:
			queryset = queryset.filter(appointment__date=app_date)

		if doctor:
			queryset = queryset.filter(appointment__doctor=doctor)

		if patient:
			queryset = queryset.filter(appointment__patient=patient)

		if patient_birthdate:
			queryset = queryset.filter(appointment__patient__birthdate=patient_birthdate)

		if is_paid:
			queryset = queryset.filter(payment_date__gte=date.today())

		return queryset


class GetAllPriceView(generics.ListAPIView):
	queryset = Price.objects.all()
	serializer_class = PriceSerializer


class GetAllCalendarView(generics.ListAPIView):
	serializer_class = Calendar

	def get_queryset(self):
		queryset = Calendar.objects.all()

		params = request.query_params

		date = params.get('date', None)

		if date:
			queryset = queryset.filter(Q(date=date) & Q(day_type='1'))

		return queryset


class GetAllCabinetView(generics.ListAPIView):
	queryset = Cabinet.objects.all()
	serializer_class = Cabinet


class UpdateAppointmentView(generics.RetrieveUpdateAPIView):
	queryset = Appointment.objects.all()
	serializer_class = CreateAppointmentSerializer


class UpdatePaymentView(generics.RetrieveUpdateAPIView):
	queryset = Payment.objects.all()
	serializer_class = PaymentSerializer


class CreateAppointmentView(generics.CreateAPIView):
	queryset = Appointment.objects.all()
	serializer_class = CreateAppointmentSerializer


class CreatePaymentView(generics.CreateAPIView):
	queryset = Payment.objects.all()
	serializer_class = CreatePaymentSerializer


class CreatePatientView(generics.CreateAPIView):
	queryset = Patient.objects.all()
	serializer_class = PatientSerializer


class CreateDoctorView(generics.CreateAPIView):
	queryset = Doctor.objects.all()
	serializer_class = CreateDoctorSerializer


class CreatePatientCardView(generics.CreateAPIView):
	queryset = PatientCard.objects.all()
	serializer_class = PatientCardSerializer


class UpdatePatientCardView(generics.RetrieveUpdateAPIView):
	queryset = PatientCard.objects.all()
	serializer_class = PatientCardSerializer
