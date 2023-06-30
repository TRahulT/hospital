from django.contrib.auth.models import Permission
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from .models import Specialty, Doctor, State, District, Village, City
from .serializers import SpecialtySerializer, DoctorSerializer, StateSerializer, DistrictSerializer, VillageSerializer, \
    CitySerializer,DoctorLoginSerializer,DoctorRegistrationSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser,AllowAny
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password

# Specialty views
@api_view(['GET', 'POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAdminUser])
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
@authentication_classes([BasicAuthentication])
@permission_classes([IsAdminUser])
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
@authentication_classes([BasicAuthentication])
@permission_classes([IsAdminUser])
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
@authentication_classes([BasicAuthentication])
@permission_classes([IsAdminUser])
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
@authentication_classes([BasicAuthentication])
@permission_classes([IsAdminUser])
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
@authentication_classes([BasicAuthentication])
@permission_classes([IsAdminUser])
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
@authentication_classes([BasicAuthentication])
@permission_classes([IsAdminUser])
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
@authentication_classes([BasicAuthentication])
@permission_classes([IsAdminUser])
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
@authentication_classes([BasicAuthentication])
@permission_classes([IsAdminUser])
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
@authentication_classes([BasicAuthentication])
@permission_classes([IsAdminUser])
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
@authentication_classes([BasicAuthentication])
@permission_classes([IsAdminUser])
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
@authentication_classes([BasicAuthentication])
@permission_classes([IsAdminUser])
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
from .models import Patient
from .serializers import PatientSerializer


@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([AllowAny])
def get_patients(request):
    patients = Patient.objects.all()
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_patient(request, pk):
    patient = Patient.objects.get(id=pk)
    serializer = PatientSerializer(patient)
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAdminUser])
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
        speciality=serializer.validated_data['speciality']
        doctor= serializer.validated_data['doctor']
        modifiedBy = serializer.validated_data['modifiedBy']
        ipAddress = serializer.validated_data.get('ipAddress')
        serializer.save()  # Set the IP address during save
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT','PATCH'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def update_patient(request, pk):
    patient = Patient.objects.get(id=pk)
    serializer = PatientSerializer(instance=patient, data=request.data,partial=True)
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
        serializer.save(modifiedBy=request.user)  # Set the IP address during save
        return Response(serializer.data)
    return Response(serializer.errors, status=400)




@api_view(['DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAdminUser])
def delete_patient(request, pk):
    patient = Patient.objects.get(id=pk)
    patient.delete()
    return Response(status=204)


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import SuperUserRegistrationSerializer, OperatorRegistrationSerializer, PatientRegistrationSerializer
@csrf_exempt
@api_view(['POST'])
def create_superuser(request):
    serializer = SuperUserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = CustomUser.objects.create_superuser(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password'],
            user_type='admin',
            is_staff=True
        )
        return Response({'message': 'Superuser created successfully.'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@csrf_exempt
@api_view(['POST'])
def create_operator(request):
    serializer = OperatorRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = CustomUser.objects.create_user(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password'],
            user_type='operator',
            is_staff=True
        )
        permissions = ['view_patient', 'add_patient', 'change_patient', 'delete_patient']
        for permission_codename in permissions:
            permission = Permission.objects.get(codename=permission_codename)
            user.user_permissions.add(permission)
        return Response({'message': 'Operator created successfully.'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def operator_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    # Authenticate the operator credentials
    user = authenticate(username=username, password=password)

    if user is not None and user.is_active and user.is_staff and user.user_type == 'operator':
        # Log in the operator
        login(request, user)

        # Return success response
        return Response({'message': 'Operator logged in successfully.'}, status=status.HTTP_200_OK)
    else:
        # Return error response
        return Response({'message': 'Invalid username or password.'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    operator = request.user
    old_password = request.data.get('old_password')
    new_password = request.data.get('new_password')

    # Verify the old password
    if not check_password(old_password, operator.password):
        return Response({'message': 'Invalid old password.'}, status=status.HTTP_400_BAD_REQUEST)

    # Change the password
    operator.set_password(new_password)
    operator.save()

    # Return success response
    return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def operator_logout(request):
    # Log out the operator
    logout(request)

    # Return success response
    return Response({'message': 'Operator logged out successfully.'}, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['POST'])
def Create_patient(request):
    serializer = PatientRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data['mobile_number']
        password = serializer.validated_data['password']
        user = CustomUser.objects.create_user(
            username=username,
            mobile_number=username,
            password=password,
            user_type='patient'
        )
        return Response({'message': 'Patient created successfully.',"registerd":"true"}, status=status.HTTP_201_CREATED)
    return Response({"msg":"Account already exists with this mobile number","status":"false"}, status=status.HTTP_400_BAD_REQUEST)



@csrf_exempt
@api_view(['POST'])
def patient_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user is not None and user.is_active and user.user_type == 'patient':
        login(request, user)
        return Response({'message': 'Patient login successful.'}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Invalid username or password.'}, status=status.HTTP_401_UNAUTHORIZED)


from rest_framework.views import APIView


class DoctorLoginView(APIView):
    def post(self, request, format=None):
        serializer = DoctorLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone_number = serializer.validated_data['phone_number']
        password = serializer.validated_data['password']

        try:
            doctor = Doctor.objects.get(phone_number=phone_number)
            print(doctor.password)
            print(password)

            if password==doctor.password:
                request.session['doctor_id'] = doctor.Doctorid
                return Response({'detail': 'Login successful.'})
            else:
                return Response({'detail': 'Invalid number or password.'}, status=status.HTTP_400_BAD_REQUEST)

        except Doctor.DoesNotExist:
            return Response({'detail': 'does  not exist .'}, status=status.HTTP_400_BAD_REQUEST)


class DoctorLogoutView(APIView):
    def post(self, request, format=None):
        if 'doctor_id' in request.session:
            del request.session['doctor_id']

        return Response({'detail': 'Logged out successfully.'})



# @api_view(['GET'])
# @authentication_classes([BasicAuthentication])
# @permission_classes([AllowAny])
# def get_patient(request, pk ,mk):
#     patients = Patient.objects.filter(doctor=mk, date=pk)
#     serializer = PatientSerializer(patients)
#     return Response(serializer.data)
#
from datetime import datetime
@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([AllowAny])
def get_patient_data(request, doctor_id, date):
    try:
        # Convert the date string to a datetime object
        search_date = datetime.strptime(date, '%Y-%m-%d').date()

        # Fetch all patients with matching doctor ID and date
        patients = Patient.objects.filter(doctor_id=doctor_id, date=search_date)

        # Serialize the patient data
        serialized_patients = []
        for patient in patients:
            serialized_patients.append({
                'id': patient.id,
                'name': patient.name,
                'dob': patient.dob,
                # Add more fields as needed
            })

        return Response(serialized_patients)
    except ValueError:
        return Response({'error': 'Invalid date format. Please provide the date in the format "YYYY-MM-DD".'})

# @csrf_exempt
# @api_view(['POST'])
# def Create_doctor(request):
#     serializer = DoctorRegistrationSerializer(data=request.data)
#     if serializer.is_valid():
#         # username = serializer.validated_data['username']
#         password = serializer.validated_data['password']
#         user = CustomUser.objects.create_user(
#             username=serializer.validated_data['username'],
#             password=password,
#             user_type='doctor'
#         )
#         return Response({'message': 'doctor created successfully.',"registerd":"true"}, status=status.HTTP_201_CREATED)
#     return Response({"msg":"Account already exists with this mobile number","status":"false"}, status=status.HTTP_400_BAD_REQUEST)

