from django.conf import settings
import random
import requests
from datetime import datetime, timedelta
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from twilio.rest import Client
from .models import OTP
from .serializers import OTPSerializer, SendOTPSerializer
from django.contrib.auth import authenticate, login, logout


@api_view(['POST'])
def send_otp(request):
    serializer = SendOTPSerializer(data=request.data)
    if serializer.is_valid():
        mobile_number = serializer.validated_data['mobile_number']

        # Check if an OTP already exists for the mobile number
        otp = OTP.objects.filter(mobile_number=mobile_number).first()

        if otp:
            # Check if the existing OTP is still valid
            if otp.expiry_time > timezone.now():
                return Response({'detail': 'OTP already sent. Please use the existing OTP.','is_otp':False }, status=status.HTTP_200_OK)

        # Generate a new OTP
        otp_code = generate_otp()

        # Set the expiry time for the OTP (2 minutes from now)
        expiry_time = timezone.now() + timedelta(minutes=2)

        # Store or update the OTP in the database
        if otp:
            otp.otp_code = otp_code
            otp.expiry_time = expiry_time
            otp.save()
        else:
            otp = OTP.objects.create(mobile_number=mobile_number, otp_code=otp_code, expiry_time=expiry_time)

        otp_serializer = OTPSerializer(otp)
        print(otp)

        # Send the OTP via Twilio
        send_otp_via_twilio(mobile_number, otp_code)
        print(otp_code)

        return Response({"OTP":otp_code,'is_otp':True}, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def verify_otp(request):
    serializer = OTPSerializer(data=request.data)
    if serializer.is_valid():
        mobile_number = serializer.validated_data['mobile_number']
        otp_code = serializer.validated_data['otp_code']

        # Retrieve the OTP from the database
        try:
            otp = OTP.objects.get(mobile_number=mobile_number)
        except OTP.DoesNotExist:
            return Response({'detail': 'OTP not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Set the expiry time for the OTP (e.g., 2 minutes from now)
        expiry_time = timezone.now() + timedelta(minutes=2)

        # Check if OTP is expired
        if otp.expiry_time < timezone.now():
            otp.delete()
            return Response({'detail': 'OTP has expired. Please request a new OTP.','is_verified':"null"}, status=status.HTTP_400_BAD_REQUEST)

        # Check if OTP matches
        if otp.otp_code != otp_code:
            return Response({'detail': 'Invalid OTP.','is_verified':'false'}, status=status.HTTP_400_BAD_REQUEST)

        # Delete the OTP and authenticate the user
        otp.delete()
        # Authenticate the user using the mobile number
        # user = authenticate(request, username=mobile_number, password=None)

    #     if user is not None:
    #         # Login the user
    #         login(request, user)
    #
    #         # ... Your further logic here ...
    #
    #         return Response({'detail': 'OTP verified. User authenticated.', 'is_verified': 'true'},
    #                         status=status.HTTP_200_OK)
    #     else:
    #         return Response({'detail': 'User authentication failed.', 'is_verified': 'false'},
    #                         status=status.HTTP_401_UNAUTHORIZED)
    # else:
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     # Authenticate the user using the mobile number (implement your authentication logic here)

        return Response({'detail': 'OTP verified. User authenticated.','is_verified':'true'}, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def resend_otp(request):
    serializer = SendOTPSerializer(data=request.data)
    if serializer.is_valid():
        mobile_number = serializer.validated_data['mobile_number']

        # Check if an OTP already exists for the mobile number
        otp = OTP.objects.filter(mobile_number=mobile_number).first()

        if otp:
            # Check if the existing OTP is still valid
            if otp.expiry_time > timezone.now():
                return Response({'detail': 'OTP already sent. Please use the existing OTP.'}, status=status.HTTP_400_BAD_REQUEST)

        # Generate a new OTP
        otp_code = generate_otp()

        # Set the expiry time for the OTP (2 minutes from now)
        expiry_time = timezone.now() + timedelta(minutes=2)

        # Store or update the OTP in the database
        if otp:
            otp.otp_code = otp_code
            otp.expiry_time = expiry_time
            otp.save()
        else:
            otp = OTP.objects.create(mobile_number=mobile_number, otp_code=otp_code, expiry_time=expiry_time)

        otp_serializer = OTPSerializer(otp)

        # Send the OTP via Twilio
        send_otp_via_twilio(mobile_number, otp_code)

        return Response(otp_serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def generate_otp():
    otp = random.randint(100000, 999999)
    return str(otp) # Replace with your OTP generation code

def send_otp_via_twilio(mobile_number,otp_code):

    # print(mobile_number)
    api_url = 'http://148.251.129.118/wapp/api/send'
    api_key = 'ddfbe5602442481d9599aa4ea927fa24'
    payload = {}
    headers = {}
    url = f'{api_url}?apikey={api_key}&mobile=91{mobile_number}&msg=Your%20OTP%20for%20verification%20is{otp_code}'
    response = requests.request("GET", url, headers=headers, data=payload)
    # response = requests.get(url)
    # print(otp_code)
    # api_key = 'ddfbe5602442481d9599aa4ea927fa24'
    # url = f'http://148.251.129.118/wapp/api/send?apikey=ddfbe5602442481d9599aa4ea927fa24&mobile=91{mobile_number}&msg=Your%20OTP%20for%20verification%20is{otp_code}'
    # # url = f"http://bulkwhatsapp.live/wapp/api/send?apikey={api_key}&mobile={mobile_number}&msg=Your OTP for Patient verification is {otp_code}. Please enter it within 10 mins. Thank you for choosing our Service "
    # res= requests.get(url)

    # account_sid = 'AC9556d1ac1720f7b093a9de843e47602c'
    # auth_token = 'f938825b0eade5c9ef9ff35ff88ca59e'
    # client = Client(account_sid, auth_token)
    # client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    # message = client.messages.create(
    #     body=f'Your OTP: {otp_code}',
    #     from_=settings.TWILIO_PHONE_NUMBER,
    #     to=mobile_number
    # )
    # message = client.messages.create(
    #     from_='whatsapp:+14155238886',
    #     body=f'Your Twilio code :is {otp_code}',
    #     to=f'whatsapp:{mobile_number}'
    # )




# @api_view(['POST'])
# def logout_view(request):
#     # Logout the user
#     logout(request)
#
#     return Response({'detail': 'User logged out.'}, status=status.HTTP_200_OK)
