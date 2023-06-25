from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from datetime import datetime, timedelta


class User(AbstractUser):
    # Add the mobile number field
    mobile_number = models.CharField(max_length=10, null=True, blank=True)

    # Add the MPIN field
    mpin = models.CharField(max_length=4, null=True, blank=True)

    def __str__(self):
        return self.username


class Admin(models.Model):
    # Add any fields specific to the Admin model
    admin_id = models.AutoField(primary_key=True)
    # Add any other fields as needed

    def __str__(self):
        return f"Admin {self.admin_id}"



class VaccinationCentre(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    working_hours = models.CharField(max_length=100, default='9am to 10pm')
    available_slots = models.IntegerField(default=10)
    slots_per_day = models.IntegerField(default=10)
    dosages_available = models.IntegerField(default=0)
    def available_slots(self):
        # Calculate the number of booked slots for this vaccination centre
        booked_slots = AppliedVaccination.objects.filter(vaccination_centre=self).count()

        # Calculate the number of available slots
        max_slots = 10
        available_slots = max_slots - booked_slots

        # Ensure the available slots is not negative
        if available_slots < 0:
            available_slots = 0

        return available_slots




class VaccinationSlot(models.Model):
    vaccination_centre = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    available_slots = models.PositiveIntegerField(default=10)

    def __str__(self):
        return f"{self.vaccination_centre} - {self.date} {self.time}"


class Dosage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    centre = models.ForeignKey(VaccinationCentre, on_delete=models.CASCADE)
    dosage_date = models.DateField()

    def __str__(self):
        return f"User: {self.user.username}, Centre: {self.centre.name}, Date: {self.dosage_date}"


class AppliedVaccination(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, default='Unknown')
    dob = models.DateField(default=date.today)
    age = models.IntegerField()
    vaccination_date = models.DateField(default=date.today)
    vaccination_type = models.CharField(max_length=10, default='Unknown')
    vaccination_centre = models.ForeignKey(VaccinationCentre, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
