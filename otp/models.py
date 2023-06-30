from django.db import models
from django.contrib.auth.models import AbstractUser

class OTP(models.Model):
    mobile_number = models.CharField(max_length=15)
    otp_code = models.CharField(max_length=6)
    expiry_time = models.DateTimeField(blank=True,null=True)


