from rest_framework import serializers
from .models import Specialty, Doctor, State, District, Village, City,OPD_Table,PatientDocument


class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'


class VillageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Village
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


from .models import Patients


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = '__all__'

class OPD_TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = OPD_Table
        fields = '__all__'


class PDFDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDocument
        fields = ('pdf_file',)




from rest_framework import serializers
from .models import CustomUser

class SuperUserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'user_type')
        extra_kwargs = {
            'password': {'write_only': True},
            'user_type': {'read_only': True}
        }

class OperatorRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'user_type')
        extra_kwargs = {
            'password': {'write_only': True},
            'user_type': {'read_only': True}
        }

class PatientRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('mobile_number', 'password', 'user_type')
        extra_kwargs = {
            'password': {'write_only': True},
            'user_type': {'read_only': True}
        }
class DoctorRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('mobile_number', 'password', 'user_type')
        extra_kwargs = {
            'password': {'write_only': True},
            'user_type': {'read_only': True}
        }



class DoctorLoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField()
