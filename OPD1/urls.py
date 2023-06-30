from django.urls import path
from .views import (
    specialty_list, specialty_detail,
    doctor_list, doctor_detail,
    state_list, state_detail,
    district_list, district_detail,
    village_list, village_detail,
    city_list, city_detail,get_districts_by_state,

    get_patients,
    get_patient,
    get_patient_data,
    create_patient,
    update_patient,
    delete_patient,
    create_superuser, create_operator, Create_patient
    ,patient_login,DoctorLoginView,DoctorLogoutView
)

urlpatterns = [
    path('specialties/', specialty_list, name='specialty-list'),
    path('specialties/<int:pk>/', specialty_detail, name='specialty-detail'),
    path('doctors/', doctor_list, name='doctor-list'),
    path('doctors/<int:pk>/', doctor_detail, name='doctor-detail'),
    path('states/', state_list, name='state-list'),
    path('states/<int:pk>/', state_detail, name='state-detail'),
    path('districts/', district_list, name='district-list'),
    path('districts/<int:pk>/', district_detail, name='district-detail'),
    path('villages/', village_list, name='village-list'),
    path('villages/<int:pk>/', village_detail, name='village-detail'),
    path('cities/', city_list, name='city-list'),
    path('cities/<int:pk>/', city_detail, name='city-detail'),
    path('district/<int:state_id>/', get_districts_by_state, name='districts-by-state'),


    # Patient data
    path('patients/', get_patients, name='get_patients'),
    path('patients/<int:pk>/', get_patient, name='get_patient'),

    # path('doctor_patient/', get_doctor_patient, name='get_patient'),
    path('patients/create/', create_patient, name='create_patient'),
    path('patients/<int:pk>/update/', update_patient, name='update_patient'),
    path('patients/<int:pk>/delete/', delete_patient, name='delete_patient'),


    # Register
    path('register/superuser/', create_superuser, name='register_superuser'),
    path('register/operator/', create_operator, name='register_operator'),
    path('register/patient/', Create_patient, name='register_patient'),
    # path('register/doctor/',Create_doctor,name='register_doctor'),


    # login Patient
    path('login/patient/', patient_login, name='patient_login'),

    path('doctor-login/', DoctorLoginView.as_view(), name='doctor_login'),
    path('doctor-logout/', DoctorLogoutView.as_view(), name='doctor_logout'),

    #doctor
    path('api/patients/<int:doctor_id>/<str:date>/', get_patient_data, name='get_patient_data'),
]
