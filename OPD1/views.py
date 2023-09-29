from fcm_django.models import FCMDevice
from rest_framework.decorators import api_view, authentication_classes, permission_classes, parser_classes
from rest_framework.generics import get_object_or_404, ListAPIView
from rest_framework.utils import json

from .models import Specialty, Doctor, State, District, Village, City,PatientDocument,OperatorReport
from .serializers import SpecialtySerializer, DoctorSerializer, StateSerializer, DistrictSerializer, VillageSerializer, \
    CitySerializer, DoctorLoginSerializer, DoctorRegistrationSerializer,OPD_Table,OPD_TableSerializer ,PDFDocumentSerializer,OperatorRecordSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password
from rest_framework.views import APIView
from django.conf import settings

from .mypagination import MyCustomPagination

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
# @authentication_classes([BasicAuthentication])
# @permission_classes([IsAdminUser])
def doctor_detail(request, pk):
    try:
        doctor = Doctor.objects.get(phone_number=pk)
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
        paginator = MyCustomPagination()
        result_page = paginator.paginate_queryset(states, request)
        serializer = StateSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
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


from django.http import JsonResponse, HttpResponse


def get_districts_by_state(request, state_id):
    districts = District.objects.filter(stateID=state_id)
    district_data = [{'id': district.Districtid, 'name': district.District_name} for district in districts]
    return JsonResponse(district_data, safe=False)



from .models import Patients
from .serializers import PatientSerializer


@api_view(['GET','POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([AllowAny])
def get_patients(request):
    if request.method == 'GET':
        patients = Patients.objects.all()
        paginator = MyCustomPagination()
        result_page = paginator.paginate_queryset(patients, request)
        serializer = PatientSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    elif request.method == 'POST':
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_patient(request, pk):
    patient = Patients.objects.get(id=pk)
    serializer = PatientSerializer(patient)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_patient_mobile(request, mobile_number):
    patient = Patients.objects.get(phone_number=mobile_number)
    serializer = PatientSerializer(patient)
    return Response(serializer.data)


class CreatePatientView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Set the IP address during save
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['PUT', 'PATCH'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def update_patient(request, pk):
    patient = Patients.objects.get(id=pk)
    serializer = PatientSerializer(instance=patient, data=request.data, partial=True)
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
        serializer.save(modifiedBy=request.user)  # Set the IP address during save
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([AllowAny])
def delete_patient(request, pk):
    patient = Patients.objects.get(id=pk)
    patient.delete()
    return Response(status=204)



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
        # permissions = ['view_patient', 'add_patient', 'change_patient', 'delete_patient']
        # for permission_codename in permissions:
        #     permission = Permission.objects.get(codename=permission_codename)
        #     user.user_permissions.add(permission)
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
        return Response({'message': 'Operator logged in successfully.', 'is_log': True}, status=status.HTTP_200_OK)
    else:
        # Return error response
        return Response({'message': 'Invalid username or password.', 'is_log': False}, status=status.HTTP_200_OK)


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
        return Response({'message': 'Patient created successfully.', "registerd": "true"},
                        status=status.HTTP_201_CREATED)
    return Response({"msg": "Account already exists with this mobile number", "status": "false"},
                    status=status.HTTP_400_BAD_REQUEST)


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

            if password == doctor.password:
                request.session['doctor_id'] = doctor.Doctorid
                return Response({'detail': 'Login successful.', 'is_loged': True})
            else:
                return Response({'detail': 'Invalid number or password.', 'is_loged': False},
                                status=status.HTTP_201_CREATED)

        except Doctor.DoesNotExist:
            return Response({'detail': 'does  not exist .', 'is_loged': False}, status=status.HTTP_400_BAD_REQUEST)


class DoctorLogoutView(APIView):
    def post(self, request, format=None):
        if 'doctor_id' in request.session:
            del request.session['doctor_id']

        return Response({'detail': 'Logged out successfully.'})


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
        patients = OPD_Table.objects.filter(doctor=doctor_id, opd_date=search_date, payment_status=True)

        # Serialize the patient data

        serialized_patients = []
        for patient in patients:
            serialized_patients.append({
                'slipID': patient.id,
                'id': patient.User_UID.id,
                'name': patient.User_UID.name,
                'Age':patient.User_UID.age,
                'opd_slip':patient.opd_slip_number,
                'opd_date':patient.opd_date,
                'opd_time':patient.opd_time
                # 'dob': patient.dob,
                # 'inputDate': patient.inputDate,
                # Add more fields as needed
            })

        return Response(serialized_patients)
    except ValueError:
        return Response({'error': 'Invalid date format. Please provide the date in the format "YYYY-MM-DD".'})
@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([AllowAny])
def get_patient_visit(request, patient_id):
    try:
        patients = OPD_Table.objects.filter(User_UID=patient_id)

        # Serialize the patient data
        serialized_patients = []
        for patient in patients:
            serialized_patients.append({
                'slipID': patient.id,
                'id': patient.User_UID.id,
                'name': patient.User_UID.name,
                'Age':patient.User_UID.age,
                'opd_slip':patient.opd_slip_number,
                'opd_date':patient.opd_date,
                'opd_time':patient.opd_time,

            })
        return Response(serialized_patients)
    except ValueError:
        return Response({'error': 'Invalid'})

@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([AllowAny])
def get_patient_by_phone_number(request, phone_number):
    try:
        patients = Patients.objects.filter(phone_number=phone_number)
        # Serialize the patient data
        serialized_patients = []
        for patient in patients:
            serialized_patients.append({
                'id': patient.id,
                'name': patient.name,
                'Age':patient.age,
            })
        return Response(serialized_patients)
    except ValueError:
        return Response({'error': 'Invalid'})

from django.http import JsonResponse
from django.middleware.csrf import get_token


def get_csrf_token(request):
    csrf_token = get_token(request)
    response = JsonResponse({'csrf_token': csrf_token})
    response["Access-Control-Allow-Origin"] = "*"  # Allow requests from any origin
    return response

# @api_view(['GET','POST'])
# @authentication_classes([BasicAuthentication])
# @permission_classes([AllowAny])
# def get_patients(request):
#     if request.method == 'GET':
#         patients = Patients.objects.all()
#         paginator = MyCustomPagination()
#         result_page = paginator.paginate_queryset(patients, request)
#         serializer = PatientSerializer(result_page, many=True)
#         return
@api_view(['GET', 'POST'])
def opd_table_list(request):
    if request.method == 'GET':
        opd_tables = OPD_Table.objects.all()
        paginator = MyCustomPagination()
        result_page = paginator.paginate_queryset(opd_tables, request)
        serializer = OPD_TableSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    elif request.method == 'POST':
        serializer = OPD_TableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([AllowAny])
def get_patient_data_date(request, date):
    try:
        # Convert the date string to a datetime object
        search_date = datetime.strptime(date, '%Y-%m-%d').date()

        # Fetch all patients with matching doctor ID and date
        patients = OPD_Table.objects.filter(opd_date=search_date)

        # Serialize the patient data

        serialized_patients = []
        for patient in patients:
            serialized_patients.append({
                'id': patient.id,
                'User_UID': patient.User_UID.id,
                'name': patient.User_UID.name,
                'Age':patient.User_UID.age,
                "speciality": patient.speciality.name,
                "doctor_First_Name": patient.doctor.first_name,
                "doctor_Last_Name": patient.doctor.last_name,
                'opd_slip':patient.opd_slip_number,
                "modifiedTime": patient.modifiedTime,
                "opd_fee": patient.opd_fee,
                'opd_date':patient.opd_date,
                'opd_time':patient.opd_time,
                "payment_type": patient.payment_type,
                "payment_status": patient.payment_status,
                # 'dob': patient.dob,
                # 'inputDate': patient.inputDate,
                # Add more fields as needed
            })
        return Response(serialized_patients)
    except ValueError:
        return Response({'error': 'Invalid date format. Please provide the date in the format "YYYY-MM-DD".'})


@api_view(['GET', 'PUT', 'DELETE'])
def opd_table_detail(request, pk):
    try:
        opd_table = OPD_Table.objects.get(pk=pk)
        if request.method == 'GET':
            serializer = OPD_TableSerializer(opd_table)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = OPD_TableSerializer(opd_table, data=request.data ,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            opd_table.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    except OPD_Table.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)



# @api_view(['GET', 'POST'])
# def patient_document_list(request):
#     if request.method == 'GET':
#         documents = PatientDocument.objects.all()
#         serializer = PDFDocumentSerializer(documents, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = PDFDocumentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#

#
@api_view(['GET',  'DELETE'])
def patient_document_detail(request, pk):
    try:
        documents = PatientDocument.objects.filter(Patient_doc_id=pk)
    except PatientDocument.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PDFDocumentSerializer(documents,many=True)
        # serializer_data = []
        # for document in documents:
        #     serializer_data.append({
        #         'slip_id':document.Patient_doc.id,
        #         'id':document.id,
        #         'pdf_file':document.pdf_file
        #     })
        return Response(serializer.data)
    elif request.method == 'DELETE':
        documents.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class ImageViewSet(ListAPIView):
#     queryset = PatientDocument.objects.all()
#     serializer_class = PDFDocumentSerializer
#
#     def post(self, request, *args, **kwargs):
#         file = request.data['pdf_file']
#         pdf_file = PatientDocument.objects.create(pdf_file=file)
#         return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)

class ImageViewSet(APIView):
    def post(self, request, patient_doc):
        # Extract the foreign key (Patient_doc) from the URL
        patient_doc_id = patient_doc
        print(patient_doc_id)

        # Check if the patient_doc_id is valid before proceeding
        try:
            opd1_patient_document = OPD_Table.objects.get(id=patient_doc_id)
            print(opd1_patient_document)
        except OPD_Table.DoesNotExist:
            return Response({'message': 'Invalid Patient_doc ID'}, status=status.HTTP_404_NOT_FOUND)

        # Combine the foreign key value with the request data
        print(opd1_patient_document.id)
        data = request.data.copy()
        data['Patient_doc'] = opd1_patient_document.id

        # request.data["pdf_file"] = pdf_file
        # # Assuming 'pdf_file' is the key for the PDF file data in the request
        pdf_file = request.data.get('pdf_file')
        data['pdf_file'] = pdf_file
        print(data)
        serializer = PDFDocumentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Uploaded'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from django.db.models import Sum

@api_view(['GET'])
def DocMoney(request, doctor_id, date):
    try:
        # Convert the date string to a datetime object
        search_date = datetime.strptime(date, '%Y-%m-%d').date()

        # Fetch all patients with matching doctor ID and date
        opd_fee_sum = OPD_Table.objects.filter(doctor=doctor_id, opd_date=search_date, payment_status=True).aggregate(Sum('opd_fee'))['opd_fee__sum']

        # Serialize the patient data
        response_data = {
            'opd_fee_sum': opd_fee_sum
        }
        return Response(response_data)
    except ValueError:
        return Response({'error': 'Invalid date format. Please provide the date in the format "YYYY-MM-DD".'})

@api_view(['GET'])
def TodayMoney(request, date):
    try:
        # Convert the date string to a datetime object
        search_date = datetime.strptime(date, '%Y-%m-%d').date()

        # Fetch all patients with matching doctor ID and date
        opd_fee_sum = OPD_Table.objects.filter(opd_date=search_date, payment_status=True).aggregate(Sum('opd_fee'))['opd_fee__sum']

        # Serialize the patient data
        response_data = {
            'opd_fee_Today': opd_fee_sum
        }
        return Response(response_data)
    except ValueError:
        return Response({'error': 'Invalid date format. Please provide the date in the format "YYYY-MM-DD".'})

@api_view(['GET',  'DELETE'])
def Operator_record_detail(request, pk):
    try:
        documents = OperatorReport.objects.filter(Patient_record_id=pk)
    except OperatorReport.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OperatorRecordSerializer(documents,many=True)
        # serializer_data = []
        # for document in documents:
        #     serializer_data.append({
        #         'slip_id':document.Patient_doc.id,
        #         'id':document.id,
        #         'pdf_file':document.pdf_file
        #     })
        return Response(serializer.data)
    elif request.method == 'DELETE':
        documents.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

import requests
class RecordViewSet(APIView):
    def post(self, request, patient_doc):
        # Extract the foreign key (Patient_doc) from the URL
        patient_record_id = patient_doc
        print(patient_record_id)

        # Check if the patient_doc_id is valid before proceeding
        try:
            opd1_patient_document = OPD_Table.objects.get(id=patient_record_id)
            print(opd1_patient_document)
        except OPD_Table.DoesNotExist:
            return Response({'message': 'Invalid Patient_ ID'}, status=status.HTTP_404_NOT_FOUND)

        # Combine the foreign key value with the request data
        print(opd1_patient_document.id)
        data = request.data.copy()
        data['Patient_record'] = opd1_patient_document.id
        category = request.data.get('category')
        data['category'] = category
        pdf_file = request.data.get('pdf_file')
        data['pdf_file'] = pdf_file
        print(data)
        push_notification_token = request.data.get('push_notification_token')
        data['push_notification_token'] = push_notification_token

        serializer = OperatorRecordSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            push_notification_token = request.data.get('push_notification_token')
            if push_notification_token:
                url = "https://fcm.googleapis.com/fcm/send"
                headers = {
                    'Authorization': f'key={settings.FCM_DJANGO_SETTINGS["FCM_SERVER_KEY"]}',
                    'Content-Type': 'application/json'
                }

                message = {
                    "notification": {
                        "title": "Bunty Bhadwa be like",
                        "body": "panii panii panii panii uncle jiiii !!! pani pila dijiyee mera galaa sukh rha hai."
                    },
                    "to": push_notification_token,
                    "data": {
                        "message": "hello Bunty seth"
                    }
                }

                response = requests.post(url, headers=headers, json=message)

                if response.status_code == 200:
                    return Response({'message': 'Report uploaded and notification sent'},
                                    status=status.HTTP_201_CREATED)
                else:
                    return Response({'message': 'Error sending notification'},
                                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response({'message': 'Report uploaded'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




            # patient = opd1_patient_document.patient  # Assuming there's a ForeignKey relationship
            # notification_data = {
            #     "title": "New Record Uploaded",
            #     "body": f"A new record has been uploaded for {patient.name}.",
            # }
            #
            # patient_device = patient.fcm_device
            # if patient_device:
            #     fcm_send_message(
            #         registration_id=patient_device.registration_id,
            #         data=notification_data,
            #   )
            # return Response({'message': 'Uploaded'}, status=status.HTTP_201_CREATED)
        #
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

