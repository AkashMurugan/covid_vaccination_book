# Generated by Django 4.0.6 on 2023-06-24 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccination', '0011_user_mpin_alter_user_mobile_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='VaccinationRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('dob', models.DateField()),
            ],
        ),
    ]
