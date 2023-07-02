from django.contrib import admin
from .models import State, District, City, Village

# # Register your models here.
# admin.site.register(State)
# admin.site.register(District)
# admin.site.register(City)


from django.contrib import admin
from .models import Specialty, Doctor, State, District, Village, City, Patients,CustomUser

admin.site.register(CustomUser)


class PatientAdmin(admin.ModelAdmin):
    list_display = (
        'Uid', 'name', 'fh_name', 'dob', 'gender', 'category', 'phone_number','aternate_number', 'state', 'district', 'city', 'village',
        'address','date', 'inputDate', 'inputBy', 'delmark','speciality','doctor', 'modifiedBy', 'modifiedTime','opd_fee','payment_type','payment_status','extra_field', 'ipAddress')

    search_fields = Patients.Searchablefield
    list_filter = Patients.FilterFields



admin.site.register(Patients, PatientAdmin)


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
