# Generated by Django 4.1.9 on 2023-06-30 17:09

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('Cityid', models.AutoField(primary_key=True, serialize=False)),
                ('City_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('Districtid', models.AutoField(primary_key=True, serialize=False)),
                ('District_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('Doctorid', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=200)),
                ('qualification', models.CharField(max_length=100)),
                ('experience', models.PositiveIntegerField()),
                ('bio', models.TextField()),
                ('profile_picture', models.ImageField(upload_to='doctor_profile_pics')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('specialityID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('Stateid', models.AutoField(primary_key=True, serialize=False)),
                ('State_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[('admin', 'Admin'), ('operator', 'Operator'), ('patient', 'Patient')], max_length=10)),
                ('mobile_number', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('Villageid', models.AutoField(primary_key=True, serialize=False)),
                ('Village_name', models.CharField(max_length=100)),
                ('DistrictID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='OPD1.district')),
            ],
        ),
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Uid', models.CharField(max_length=36, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('fh_name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=7)),
                ('category', models.CharField(choices=[('GEN', 'General'), ('OBC', 'OBC'), ('SC', 'SC & ST')], max_length=5)),
                ('phone_number', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now=True)),
                ('inputDate', models.CharField(max_length=30)),
                ('inputBy', models.CharField(blank=True, max_length=50, null=True)),
                ('delmark', models.BooleanField(default=True)),
                ('modifiedTime', models.DateTimeField(blank=True, null=True)),
                ('ipAddress', models.GenericIPAddressField(default='192.168.0.1')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='OPD1.city')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OPD1.district')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OPD1.doctor')),
                ('modifiedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('speciality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OPD1.specialty')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OPD1.state')),
                ('village', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='OPD1.village')),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OPD1.specialty'),
        ),
        migrations.AddField(
            model_name='district',
            name='stateID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OPD1.state'),
        ),
        migrations.AddField(
            model_name='city',
            name='DistrictID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='OPD1.district'),
        ),
    ]
