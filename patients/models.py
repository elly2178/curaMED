from django.db import models
from django.urls import reverse

# Create your models here.
class PatientInformation(models.Model):
    sex=[('male','Herr'),('female','Frau')]
    title =  models.CharField(max_length=6, choices=sex)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    language = models.CharField(max_length=10)
    

    def get_absolute_url(self):
        return reverse("patients", kwargs={"id":id})

