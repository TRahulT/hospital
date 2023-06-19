from django.contrib import admin
from .models import State, District, City, Village

# # Register your models here.
# admin.site.register(State)
# admin.site.register(District)
# admin.site.register(City)


from django.contrib import admin
from .models import Specialty, Doctor, State, District, Village, City, Patient, CustomUser

admin.site.register(CustomUser)


class PatientAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'fh_name', 'dob', 'gender', 'category', 'phone_number', 'state', 'district', 'city', 'village',
        'address')


admin.site.register(Patient, PatientAdmin)


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('specialityID', 'name')


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        'Doctorid', 'first_name', 'last_name', 'email', 'phone_number', 'address', 'specialty', 'qualification',
        'experience', 'bio', 'created_at', 'updated_at')


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('Stateid', 'State_name')


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('Districtid', 'District_name', 'stateID')


@admin.register(Village)
class VillageAdmin(admin.ModelAdmin):
    list_display = ('Villageid', 'Village_name', 'DistrictID')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('Cityid', 'City_name', 'DistrictID')
