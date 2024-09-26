from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Room(models.Model):
    class Meta:
        db_table = 'Room'
    number=models.IntegerField()
    type=models.CharField(max_length=15)
    cost=models.IntegerField()
    phone=models.IntegerField()
    floor=models.IntegerField()

    def __str__(self):
        return str(self.number)

class Client(models.Model):
    class Meta:
        db_table = 'client'
    fio=models.CharField(max_length=50)
    hometown=models.CharField(max_length=15)
    passport=models.IntegerField()

    def __str__(self):
        return self.fio

class Journal(models.Model):
    class Meta:
        db_table = 'journal'
    client=models.ForeignKey(Client, on_delete=models.CASCADE)
    room=models.ForeignKey(Room, on_delete=models.CASCADE)
    checkin=models.DateField(default='2020-06-06')
    checkout=models.DateField(default='2020-06-07')

class Worker(models.Model):
    class Meta:
        db_table = 'worker'
    fio=models.CharField(max_length=50)

    def __str__(self):
        return self.fio

class Worktable(models.Model):
    class Meta:
        db_table = 'worktable'
    worker=models.ForeignKey(Worker,on_delete=models.CASCADE)
    floor=models.IntegerField()
    weekday=models.CharField(max_length=10)

    def __str__(self):
        return str(self.id)
