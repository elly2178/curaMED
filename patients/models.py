from django.db import models
from django.urls import reverse
 

class PatientInformation(models.Model):
    sex=[('male','Herr'),('female','Frau')]
    title =  models.CharField(max_length=6,choices=sex)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    address = models.CharField(max_length=50)
    number = models.CharField(max_length=10)
    city = models.CharField(max_length=25)
    code = models.CharField(max_length=4)
    language = models.CharField(max_length=50)
   

    def get_absolute_url(self):
        return reverse("patients", kwargs={"id":self.id})