from django.db import models
from django.urls import reverse

# Create your models here.
class ModalitiesInformation(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=400)
    status = models.CharField(max_length=15)

    def get_absolute_url(self):
        return reverse ("modalities", kwargs={"id":self.id})