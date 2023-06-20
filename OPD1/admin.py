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
        'address', 'inputDate', 'inputBy', 'delmark', 'modifiedBy', 'modifiedTime','ipAddress')

    search_fields = Patient.Searchablefield
    list_filter = Patient.FilterFields



admin.site.register(Patient, PatientAdmin)


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('specialityID', 'name')
    search_fields = Specialty.Searchablefield


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        'Doctorid', 'first_name', 'last_name', 'email', 'phone_number', 'address', 'specialty', 'qualification',
        'experience', 'bio', 'created_at', 'updated_at')
    # search_fields = Doctor.doctorsearch


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('Stateid', 'State_name')
    search_fields = State.searchablefield


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('Districtid', 'District_name', 'stateID')
    # search_fields = District.Searchablefield


@admin.register(Village)
class VillageAdmin(admin.ModelAdmin):
    list_display = ('Villageid', 'Village_name', 'DistrictID')
    # search_fields = Village.villagesearch



@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('Cityid', 'City_name', 'DistrictID')
    # search_fields = City.citysearch
