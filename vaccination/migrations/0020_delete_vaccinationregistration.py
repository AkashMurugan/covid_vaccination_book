# Generated by Django 4.0.6 on 2023-06-25 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vaccination', '0019_appliedvaccination_dob_appliedvaccination_gender_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='VaccinationRegistration',
        ),
    ]
