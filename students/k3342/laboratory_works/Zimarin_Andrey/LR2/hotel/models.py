from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    passport = models.CharField('Номер паспорта', max_length=20)
    full_name = models.CharField('ФИО', max_length=50)
    city = models.CharField('Из города', max_length=20)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Worker(models.Model):
    full_name = models.CharField('ФИО', max_length=50)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'


class Floor(models.Model):
    floor_num = models.IntegerField('Номер этажа')

    def __str__(self):
        return str(self.floor_num)

    class Meta:
        verbose_name = 'Этаж'
        verbose_name_plural = 'Этажи'


class Room(models.Model):
    room_number = models.IntegerField('Номер комнаты')
    floor = models.ForeignKey(Floor, verbose_name='Этаж', on_delete=models.CASCADE, related_name='rooms')
    phone = models.IntegerField('Телефон')
    price = models.IntegerField('Стоимость за сутки')
    TYPES = (('1-комн', 'Однокомнатный'),
             ('2-комн', 'Двухкомнатный'),
             ('3-комн', 'Трехкомнатный'),
             )
    type = models.CharField(max_length=20, choices=TYPES)
    client = models.ManyToManyField(Client, through='Checkin')

    def __str__(self):
        return str(self.room_number)

    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'


class Cleaning(models.Model):
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, verbose_name="Этаж", null=True)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, verbose_name="Работник")
    DAYS = (('Пон', 'Понедельник'),
            ('Вт', 'Вторник'),
            ('Ср', 'Среда'),
            ('Чт', 'Четверг'),
            ('Пт', 'Пятница'),
            ('Сб', 'Суббота'),
            ('Вс', 'Воскресенье'),
            )
    day_of_week = models.CharField(max_length=20, choices=DAYS)

    def __str__(self):
        return f"{self.worker} - {self.floor} - {self.day_of_week}"

    class Meta:
        verbose_name = 'Уборка'
        verbose_name_plural = 'Уборки'


class Checkin(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент', related_name='checkins')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Номер комнаты', related_name='checkins')
    date_in = models.DateField('Дата заселения')
    date_out = models.DateField('Дата выезда')

    def __str__(self):
        return f"{self.client} - {self.room}"

    class Meta:
        verbose_name = 'Заселение'
        verbose_name_plural = 'Заселения'
