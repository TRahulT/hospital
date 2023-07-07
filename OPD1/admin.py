from django.contrib import admin
from .models import State, District, City, Village

# # Register your models here.
# admin.site.register(State)
# admin.site.register(District)
# admin.site.register(City)


from django.contrib import admin
from .models import Specialty, Doctor, State, District, Village, City, Patients, CustomUser, OPD_Table

admin.site.register(CustomUser)


class PatientAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'fh_name', 'dob', 'gender', 'category', 'phone_number', 'aternate_number', 'state', 'district',
        'city', 'village',
        'address', 'date', 'inputDate', 'inputBy', 'extra_field', 'ipAddress')

    search_fields = Patients.Searchablefield
    list_filter = Patients.FilterFields


admin.site.register(Patients, PatientAdmin)


class OPDAdmin(admin.ModelAdmin):
    list_display = (
                    'User_UID', 'opd_slip_number', 'delmark', 'speciality', 'doctor', 'modifiedBy', 'modifiedTime', 'opd_fee',
                    'opd_time', 'opd_date', 'payment_type', 'payment_status')
    search_fields = OPD_Table.Searchablefield


admin.site.register(OPD_Table, OPDAdmin)


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
