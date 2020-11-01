from django.db import models
from django.urls import reverse
# for saving phonenumbers with correct country code
#from phonenumber_field.modelfields import PhoneNumberField

# Create your models here., Importable
class PatientInformation(models.Model):
    sex=[('male','Herr'),('female','Frau')]
    title =  models.CharField(max_length=6,choices=sex)
    name = models.CharField(max_length=50)
    vorname = models.CharField(max_length=50)
    geburtsdatum = models.DateField()
    adresse = models.CharField(max_length=50)
    plz = models.CharField(max_length=4)
    language = models.CharField(max_length=10)
    #telefon = PhoneNumberField(null=False, blank=False, unique=True)
    

    def get_absolute_url(self):
        return reverse("patients", kwargs={"id":id})

