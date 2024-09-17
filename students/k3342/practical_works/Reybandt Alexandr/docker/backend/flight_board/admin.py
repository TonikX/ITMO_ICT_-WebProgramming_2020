from django.contrib import admin

from .models import Employee, AirlineCompany, Crew, Airplane, Flight

admin.site.register(Employee)
admin.site.register(AirlineCompany)
admin.site.register(Crew)
admin.site.register(Airplane)
admin.site.register(Flight)
