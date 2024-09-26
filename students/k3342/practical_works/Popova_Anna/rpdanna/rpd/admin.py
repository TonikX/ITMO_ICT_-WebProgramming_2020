from django.contrib import admin

from .models import CarOwner
from .models import Car
from .models import DrivingLicense
from .models import Ownership

admin.site.register(CarOwner)
admin.site.register(Car)
admin.site.register(DrivingLicense)
admin.site.register(Ownership)