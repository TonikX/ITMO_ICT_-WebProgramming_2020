from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model


class Owner(AbstractUser):

    class Meta:
        db_table = 'Owner'

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField(default='1998-04-20')
    passport = models.IntegerField()
    address = models.CharField(max_length=120)
    nationality = models.CharField(max_length=20)

    def __str__(self):
        full_name = self.first_name + ' ' + self.last_name
        return full_name


class DriversLicense(models.Model):

    class Meta:
        db_table = 'DriversLicense'

    CLASSES_OF_LICENSES = (('A', 'Class A'),
                           ('B', 'Class B'),
                           ('C', 'Class C'),
                           ('D', 'Class D'),
                           ('M', 'Class M'),
                           ('ACDL', 'Class A CDL'),
                           ('BCDL', 'Class B CDL'),
                           ('CCDL', 'Class C CDL'),
                           ('MCDL', 'Class M CDL'))
    date_of_issue = models.DateField()
    license_number = models.IntegerField()
    category = models.CharField(max_length=4, choices=CLASSES_OF_LICENSES)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        license_number_str = str(self.license_number)
        return license_number_str


class Car(models.Model):

    class Meta:
        db_table = 'Car'

    model = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    car_number = models.CharField(max_length=7)
    owners = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Ownership') 

    def __str__(self):
        return self.car_number

class Ownership(models.Model):

    class Meta:
        db_table = 'Ownership'

    date_of_start = models.DateField()
    date_of_end = models.DateField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
