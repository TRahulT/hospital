# otp/serializers.py

from rest_framework import serializers
from .models import OTP

class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = '__all__'

class SendOTPSerializer(serializers.Serializer):
    mobile_number = serializers.CharField(max_length=15)
