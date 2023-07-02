from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.http import HttpRequest
from django.contrib import admin
import uuid


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('operator', 'Operator'),
        ('patient', 'Patient'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    mobile_number = models.CharField(max_length=15, unique=True , null=True, blank=True)




class Specialty(models.Model):
    specialityID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    Searchablefield = ['specialityID', 'name']

    def __str__(self):
        return self.name


class Doctor(models.Model):
    Doctorid = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=128)
    address = models.CharField(max_length=200)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=100)
    experience = models.PositiveIntegerField()
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='doctor_profile_pics')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    doctorsearch = ['first_name', 'last_name', 'phone_number', 'email', 'specialty']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class State(models.Model):
    Stateid = models.AutoField(primary_key=True)
    State_name = models.CharField(max_length=100)
    searchablefield = ['Stateid', 'State_name']

    def __str__(self):
        return self.State_name


class District(models.Model):
    Districtid = models.AutoField(primary_key=True)
    District_name = models.CharField(max_length=100)
    stateID = models.ForeignKey(State, on_delete=models.CASCADE)
    Searchablefield = ['District_name', 'stateID']

    def __str__(self):
        return self.District_name


class Village(models.Model):
    Villageid = models.AutoField(primary_key=True)
    Village_name = models.CharField(max_length=100)
    DistrictID = models.ForeignKey(District, on_delete=models.CASCADE, blank=True, null=True)
    villagesearch = ['Villageid', 'Village_name', 'DistrictID']

    def __str__(self):
        return self.Village_name


class City(models.Model):
    Cityid = models.AutoField(primary_key=True)
    City_name = models.CharField(max_length=100)
    DistrictID = models.ForeignKey(District, on_delete=models.CASCADE, blank=True, null=True)
    citysearch = ['Cityid', 'City_name', 'DistrictID']

    def __str__(self):
        return self.City_name


class Patients(models.Model):
    Uid = models.CharField(max_length=5, unique=True, null=True, blank=True)
    name = models.CharField(max_length=50)
    fh_name = models.CharField(max_length=50)
    dob = models.DateField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES)
    CATEGORY_CHOICES = (
        ('GEN', 'General'),
        ('OBC', 'OBC'),
        ('SC', 'SC & ST'),
    )
    category = models.CharField(max_length=5, choices=CATEGORY_CHOICES)
    phone_number = models.IntegerField()
    aternate_number = models.IntegerField(blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    village = models.ForeignKey(Village, on_delete=models.CASCADE, blank=True, null=True)
    address = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    inputDate = models.CharField(max_length=30)
    inputBy = models.CharField(max_length=50, null=True,blank=True)
    delmark = models.BooleanField(default=True)
    speciality = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    modifiedBy = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True)
    modifiedTime = models.DateTimeField(blank=True, null=True)
    opd_fee = models.IntegerField()
    payment_type = models.CharField(max_length=30)
    payment_status = models.BooleanField(default=False)
    ipAddress = models.GenericIPAddressField(default='192.168.0.1')
    extra_field=models.CharField(max_length=100, blank=True, null=True)
    extra_field2 = models.CharField(max_length=100, blank=True, null=True)
    Searchablefield = ['Uid', 'name', 'phone_number']
    FilterFields = ['state']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.Uid:  # Generate Uid only if it's not already set
            self.Uid = str(uuid.uuid4())[:5]

        if not self.inputBy:
            self.inputBy = self.name
        if self.pk is not None:
            original = Patients.objects.get(pk=self.pk)
            if original.inputDate:
                self.inputDate = original.inputDate
        super().save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     if not self.inputBy:
    #         self.inputBy = self.name
    #
    #     if self.pk and not self.modifiedBy:
    #         # Get the current logged-in user
    #         user = User.objects.get(username=self._get_current_username())
    #
    #         # Set the modifiedBy field to the user
    #         self.modifiedBy = user
    #
    #     super().save(*args, **kwargs)

    # def _get_current_username(self):
    #     # Assuming you have access to the Django request object
    #     # and you are using Django's built-in authentication system
    #
    #     # Check if the request object is available
    #     if hasattr(self, 'request') and self.request is not None:
    #         # Assuming you have a request object available in the model instance
    #         # and the user is authenticated
    #         if self.request.user.is_authenticated:
    #             # Retrieve the username from the authenticated user
    #             return self.request.user.username
    #
    #     # If the request object is not available or the user is not authenticated, return a default value or handle the case as per your requirement
    #     return "default_username"


@receiver(pre_save, sender=Patients)
def update_modified_time(sender, instance, **kwargs):
    if instance.pk:  # Check if the instance already exists
        instance.modifiedTime = timezone.now()
    else:
        instance.modifiedTime = None


