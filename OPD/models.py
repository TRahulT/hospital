from django.db import models


class CustomAutoField(models.AutoField):
    def get_next_value(self, *args, **kwargs):
        if self.model.objects.exists():
            last_district_id = self.model.objects.order_by('-id').first().id
            return last_district_id + 1
        else:
            return 10000


class Specialty(models.Model):
    specialityID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    Doctorid = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=100)
    experience = models.PositiveIntegerField()
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='doctor_profile_pics')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class State(models.Model):
    Stateid = models.AutoField(primary_key=True)
    State_name = models.CharField(max_length=100)

    def __str__(self):
        return self.State_name


class District(models.Model):
    Districtid = models.AutoField(primary_key=True)
    District_name = models.CharField(max_length=100)
    stateID = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.District_name


class Village(models.Model):
    Villageid = models.AutoField(primary_key=True)
    Village_name = models.CharField(max_length=100)
    DistrictID = models.ForeignKey(District, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.Village_name


class City(models.Model):
    Cityid = models.AutoField(primary_key=True)
    City_name = models.CharField(max_length=100)
    DistrictID = models.ForeignKey(District, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.City_name


class Patient(models.Model):
    id = CustomAutoField(primary_key=True)
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
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    village = models.ForeignKey(Village, on_delete=models.CASCADE, blank=True, null=True)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # Add your additional fields here
    is_limited_user = models.BooleanField(default=False)
