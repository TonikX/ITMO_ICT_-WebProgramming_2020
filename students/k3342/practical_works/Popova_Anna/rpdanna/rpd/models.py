from django.db import models

class CarOwner(models.Model):
    '''
    Модель для автовладельца
    '''
    firstname = models.CharField(max_length=1024)
    lastname = models.CharField(max_length=1024)
    birthdate = models.DateField(auto_now=False, auto_now_add=False)

class Car(models.Model):
    '''
    Модел для машины
    '''
    brand = models.CharField(max_length=1024)
    car_model = models.CharField(max_length=1024)
    color = models.CharField(max_length=1024)
    gov_number = models.IntegerField()

class Ownership(models.Model):
    '''
    Модель для владения
    '''
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        unique_together = ('owner', 'car')

class DrivingLicense(models.Model):
    '''
    Модель для вод. удостоверения
    '''
    license_number = models.IntegerField()
    starting_date = models.DateField(auto_now=False, auto_now_add=False)
    type = [
        ('1', 'First type'),
        ('2', 'Second type'),
        ('3', 'Third type'),
    ]
    typelevel = models.CharField(
        max_length=1,
        choices=type,
        default=1,
    )
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
