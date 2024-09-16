from django.contrib import admin
from project_first_app.models import Owner, DriversLicense, Car, Ownership


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth')
    list_display_links = ('first_name', 'last_name', 'date_of_birth')


class DriversLicenseAdmin(admin.ModelAdmin):
    list_display = ('owner', 'date_of_issue', 'category', 'license_number')
    list_display_links = ('owner', 'date_of_issue', 'category', 'license_number')


class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'color', 'car_number')
    list_display_links = ('model', 'brand', 'color', 'car_number')


class OwnershipAdmin(admin.ModelAdmin):
    list_display = ('owner', 'car', 'date_of_start', 'date_of_end')
    list_display_links = ('owner', 'car', 'date_of_start', 'date_of_end')


admin.site.register(Owner, OwnerAdmin)
admin.site.register(DriversLicense, DriversLicenseAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Ownership, OwnershipAdmin)
