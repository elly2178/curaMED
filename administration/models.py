from django.db import models
from django.urls import reverse
# Create your models here.
class AdministrationInformation(models.Model):
    street = models.CharField(max_length=80)
    city = models.CharField(max_length=40)
    plz = models.CharField(max_length=15)
    number = models.IntegerField()

    def get_absolute_url(self):
        return reverse("administration", kwargs={"id":self.id})