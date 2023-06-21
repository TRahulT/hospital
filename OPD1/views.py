from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Specialty, Doctor, State, District, Village, City
from .serializers import SpecialtySerializer, DoctorSerializer, StateSerializer, DistrictSerializer, VillageSerializer, \
    CitySerializer


# Specialty views
@api_view(['GET', 'POST'])
def specialty_list(request):
    if request.method == 'GET':
        specialties = Specialty.objects.all()
        serializer = SpecialtySerializer(specialties, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SpecialtySerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            # otp_code = serializer.validated_data['otp_code']
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def specialty_detail(request, pk):
    try:
        specialty = Specialty.objects.get(pk=pk)
    except Specialty.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = SpecialtySerializer(specialty)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SpecialtySerializer(specialty, data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        specialty.delete()
        return Response(status=204)


# Doctor views
@api_view(['GET', 'POST'])
def doctor_list(request):
    if request.method == 'GET':
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':

        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            first_name = serializer.validated_data['first_name']
            last_name = serializer.validated_data['last_name']
            email = serializer.validated_data['email']
            phone_number = serializer.validated_data['phone_number']
            password = serializer.validated_data['password']
            address = serializer.validated_data['address']
            specialty = serializer.validated_data['specialty']
            qualification = serializer.validated_data['qualification']
            experience = serializer.validated_data['experience']
            bio = serializer.validated_data['bio']
            profile_picture = serializer.validated_data['profile_picture']
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def doctor_detail(request, pk):
    try:
        doctor = Doctor.objects.get(pk=pk)
    except Doctor.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DoctorSerializer(doctor, data=request.data)
        if serializer.is_valid():
            first_name = serializer.validated_data['first_name']
            last_name = serializer.validated_data['last_name']
            email = serializer.validated_data['email']
            phone_number = serializer.validated_data['phone_number']
            password = serializer.validated_data['password']
            address = serializer.validated_data['address']
            specialty = serializer.validated_data['specialty']
            qualification = serializer.validated_data['qualification']
            experience = serializer.validated_data['experience']
            bio = serializer.validated_data['bio']
            profile_picture = serializer.validated_data['profile_picture']
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        doctor.delete()
        return Response(status=204)


# Similarly, define views for State, District, Village, and City models

# State views
@api_view(['GET', 'POST'])
def state_list(request):
    if request.method == 'GET':
        states = State.objects.all()
        serializer = StateSerializer(states, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def state_detail(request, pk):
    try:
        state = State.objects.get(pk=pk)
    except State.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = StateSerializer(state)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = StateSerializer(state, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        state.delete()
        return Response(status=204)


# District views
@api_view(['GET', 'POST'])
def district_list(request):
    if request.method == 'GET':
        districts = District.objects.all()
        serializer = DistrictSerializer(districts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DistrictSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def district_detail(request, pk):
    try:
        district = District.objects.get(pk=pk)
    except District.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = DistrictSerializer(district)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DistrictSerializer(district, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        district.delete()
        return Response(status=204)


# Village views
@api_view(['GET', 'POST'])
def village_list(request):
    if request.method == 'GET':
        villages = Village.objects.all()
        serializer = VillageSerializer(villages, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = VillageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def village_detail(request, pk):
    try:
        village = Village.objects.get(pk=pk)
    except Village.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = VillageSerializer(village)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = VillageSerializer(village, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        village.delete()
        return Response(status=204)


# City views
@api_view(['GET', 'POST'])
def city_list(request):
    if request.method == 'GET':
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def city_detail(request, pk):
    try:
        city = City.objects.get(pk=pk)
    except City.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = CitySerializer(city)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CitySerializer(city, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        city.delete()
        return Response(status=204)


from django.http import JsonResponse


def get_districts_by_state(request, state_id):
    districts = District.objects.filter(stateID=state_id)
    district_data = [{'id': district.Districtid, 'name': district.District_name} for district in districts]
    return JsonResponse(district_data, safe=False)


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Patient
from .serializers import PatientSerializer


@api_view(['GET'])
def get_patients(request):
    patients = Patient.objects.all()
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_patient(request, pk):
    patient = Patient.objects.get(id=pk)
    serializer = PatientSerializer(patient)
    return Response(serializer.data)


@api_view(['POST'])
def create_patient(request):
    serializer = PatientSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        fh_name = serializer.validated_data['fh_name']
        dob = serializer.validated_data['dob']
        gender = serializer.validated_data['gender']
        category = serializer.validated_data['category']
        phone_number = serializer.validated_data['phone_number']
        state = serializer.validated_data['state']
        district = serializer.validated_data['district']
        city = serializer.validated_data['city']
        village = serializer.validated_data['village']
        address = serializer.validated_data['address']
        delmark = serializer.validated_data['delmark']
        modifiedBy = serializer.validated_data['modifiedBy']
        ipAddress = serializer.validated_data.get('ipAddress')
        serializer.save()  # Set the IP address during save
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT','PATCH'])
def update_patient(request, pk):
    patient = Patient.objects.get(id=pk)
    serializer = PatientSerializer(instance=patient, data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        fh_name = serializer.validated_data['fh_name']
        dob = serializer.validated_data['dob']
        gender = serializer.validated_data['gender']
        category = serializer.validated_data['category']
        phone_number = serializer.validated_data['phone_number']
        state = serializer.validated_data['state']
        district = serializer.validated_data['district']
        city = serializer.validated_data['city']
        village = serializer.validated_data['village']
        address = serializer.validated_data['address']
        delmark= serializer.validated_data['delmark']
        modifiedBy = serializer.validated_data['modifiedBy']
        ipAddress = serializer.validated_data.get('ipAddress') # Get the client IP address
        serializer.save()  # Set the IP address during save
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delete_patient(request, pk):
    patient = Patient.objects.get(id=pk)
    patient.delete()
    return Response(status=204)
