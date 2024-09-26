from django.contrib import admin
from hotel.models import Room, Client, Worker, Floor, Cleaning, Checkin
# Register your models here.


class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'floor', 'price', 'type')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'passport', 'city')


admin.site.register(Room, RoomAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Floor)
admin.site.register(Worker)
admin.site.register(Cleaning)
admin.site.register(Checkin)
