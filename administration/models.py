from django.db import models
from django.urls import reverse
from django.forms import ModelChoiceField 

class LocationModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.street} {obj.number}, {obj.city}"
        

class AdministrationInformation(models.Model):
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=80)
    city = models.CharField(max_length=40)
    plz = models.CharField(max_length=4) 
    number = models.IntegerField() 
    telefon_number = models.CharField(max_length=30)

    def get_absolute_url(self):
        return reverse("administration", kwargs={"id":self.id})

    def get_location_representation(self):
        return f"{self.street} {self.number}, {self.city}"