from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError

#validation
def validate_port(value):
    if 0 <= value <= 65535:
        return value
    else:
        raise ValidationError('Port value out of range')
# Create your models here.
class ModalitiesInformation(models.Model):
    title = models.CharField(max_length=150)
    ae_title = models.CharField(max_length=15)
    description = models.TextField(max_length=400)
    ip = models.GenericIPAddressField()
    port = models.PositiveIntegerField(validators = [validate_port])
    associate_location = models.ForeignKey('administration.AdministrationInformation', on_delete=models.CASCADE)
   

    def get_absolute_url(self):
        return reverse ("modalities", kwargs={"id":self.id})