# Generated by Django 4.1.9 on 2023-06-13 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='expiry_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
