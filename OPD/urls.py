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
    create_patient,
    update_patient,
    delete_patient,
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
    path('patients/', get_patients, name='get_patients'),
    path('patients/<int:pk>/', get_patient, name='get_patient'),
    path('patients/create/', create_patient, name='create_patient'),
    path('patients/<int:pk>/update/', update_patient, name='update_patient'),
    path('patients/<int:pk>/delete/', delete_patient, name='delete_patient'),

]
