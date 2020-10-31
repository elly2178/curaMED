from django.contrib import admin

# Register your models here.
from .models import PatientInformation

admin.site.register(PatientInformation)