from django.contrib import admin

# Register your models here.

from .models import Car, Owner, License, Owning
admin.site.register(Car)
admin.site.register(Owner)
admin.site.register(License)
admin.site.register(Owning)
