from django.contrib.auth.models import AbstractUser, User
from django.db import models

import uuid


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('operator', 'Operator'),
        ('patient', 'Patient'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    mobile_number = models.CharField(max_length=15, unique=True, null=True, blank=True)


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
    profile_picture = models.CharField(max_length=300)
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


def generate_Uid():
    opd_slip_number = str(uuid.uuid4())[:5]  # Generate a random UUID and extract the first 5 digits
    return opd_slip_number


class Patients(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField(max_length=50)
    fh_name = models.CharField(max_length=50)
    dob = models.DateField()
    age = models.CharField(max_length=50)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES)
    category = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    aternate_number = models.IntegerField(blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    village = models.ForeignKey(Village, on_delete=models.CASCADE, blank=True, null=True)
    address = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    inputDate = models.CharField(max_length=30)
    inputBy = models.CharField(max_length=50, null=True, blank=True)
    ipAddress = models.GenericIPAddressField(default='192.168.0.1')
    extra_field = models.CharField(max_length=100, blank=True, null=True)
    extra_field2 = models.CharField(max_length=100, blank=True, null=True)

    # fcm_device = models.OneToOneField(FCMDevice, on_delete=models.SET_NULL, null=True)

    Searchablefield = ['id', 'name', 'phone_number']
    FilterFields = ['state']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # if not self.Uid:  # Generate Uid only if it's not already set
        #     self.Uid = str(uuid.uuid4())[:5]

        if not self.inputBy:
            self.inputBy = self.name
        # if self.id is not None:
        #     original = Patients.objects.get(pk=self.id)
        #     if original.id:
        #         self.id = original.id
        super().save(*args, **kwargs)


def generate_opd_slip_number():
    # global slip_number
    # if 'slip_number' not in globals():
    #     slip_number = 100000
    # else:
    #     slip_number += 1
    # opd_slip_number = str(slip_number)
    # return opd_slip_number
    opd_slip_number = str(uuid.uuid4())[
                      :5]  # str(uuid.uuid4().int)[:5]  # Generate a random UUID and extract the first 6 digits
    return opd_slip_number


class OPD_Table(models.Model):
    User_UID = models.ForeignKey(Patients, on_delete=models.CASCADE)
    opd_slip_number = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    delmark = models.BooleanField(default=True)
    speciality = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    modifiedBy = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    modifiedTime = models.DateTimeField(blank=True, null=True)
    opd_fee = models.IntegerField()
    opd_date = models.DateField(auto_now_add=True)
    opd_time = models.TimeField(auto_now_add=True)
    payment_type = models.CharField(max_length=30)
    payment_status = models.BooleanField(default=False)
    push_notification_token = models.CharField(max_length=255, blank=True, null=True)
    Searchablefield = ['opd_slip_number', 'User_UID', 'opd_date']


class PatientDocument(models.Model):
    Patient_doc = models.ForeignKey(OPD_Table, on_delete=models.CASCADE)
    pdf_file = models.FileField(upload_to='pdf_uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class OperatorReport(models.Model):
    Patient_record = models.ForeignKey(OPD_Table, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    pdf_file = models.FileField(upload_to='report_upload/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


# class Insurance(models.Model):
#     category = models.CharField(max_length=50)
#
#
# class AddFee(models.Model):
#     Specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
#     Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     Day = models.CharField(max_length=20)
#     Category = models.ForeignKey(Insurance, on_delete=models.CASCADE)
#     fee = models.IntegerField()


# @receiver(post_save, sender=PatientSlip)
# def send_notification_on_slip_upload(sender, instance, created, **kwargs):
#     if created:
#         patient_name = instance.patient.name  # Update this based on your Patient model field
#         message = messaging.Message(
#             notification=messaging.Notification(
#                 title="Medical Reports Uploaded",
#                 body=f"Your Medical Reports are uploaded, {patient_name}. Please Checkout!",
#             ),
#             topic=instance.patient.id,  # Assuming patient.id is unique and can be used as a topic
#         )
#         response = messaging.send(message)
#         print('Notification sent:', response)

# fee table doctor + category , ses
