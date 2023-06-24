from django.contrib import admin
from .models import *


admin.site.register(User)
admin.site.register(VaccinationCentre)
admin.site.register(AppliedVaccination)
admin.site.register(VaccinationRegistration)

