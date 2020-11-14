from django.db import models
from django.urls import reverse
from django.forms import ModelChoiceField


class StandortModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.street} {obj.number}, {obj.city}"
        

class AdministrationInformation(models.Model):
    # order of the elements --> different
    # for loop for showing location --> latest first
    # set default one of them--> last added
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=80)
    city = models.CharField(max_length=40)
    plz = models.CharField(max_length=4)
    number = models.IntegerField()
    telefon_number = models.CharField(max_length=10)

    def get_absolute_url(self):
        return reverse("administration", kwargs={"id":self.id})