from django.db import models

# Create your models here.
class ModalitiesInformation(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=400)
    status = models.CharField(max_length=15)