from django.db import models
from django.urls import reverse
# for saving phonenumbers with correct country code
#from phonenumber_field.modelfields import PhoneNumberField

# Create your models here., Importable
class PatientInformation(models.Model):
    sex=[('male','Herr'),('female','Frau')]
    title =  models.CharField(max_length=6,choices=sex)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    address = models.CharField(max_length=50)
    code = models.CharField(max_length=4)
    language = models.CharField(max_length=10)
    #telefon = PhoneNumberField(null=False, blank=False, unique=True)
    

    def get_absolute_url(self):
        return reverse("patients", kwargs={"id":self.id})

