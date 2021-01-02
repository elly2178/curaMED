from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.forms import ModelChoiceField

class ModalityModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.title}, {obj.description} [{obj.ae_title}]"  

#validation
def validate_port(value):
    if 0 <= value <= 65535:
        return value
    else:
        raise ValidationError("Port Nummer muss zwischen 0 und 65535 liegen.")

class ModalitiesInformation(models.Model):
    types = [('CR',' Computerradiografie '),
    ('CT','Computertomografie'),
    ('US','Ultraschall'),
    ('ES','Endoskopie'),
    ('DX','Digitale Radiografie'),
    ('MG','Mammografie')    
    ]
    title = models.CharField(max_length=150, choices=types)
   
    ae_title = models.CharField(max_length=15)
    description = models.TextField(max_length=400)
    ip = models.GenericIPAddressField()
    port = models.PositiveIntegerField(validators = [validate_port])
    associate_location = models.ForeignKey('administration.AdministrationInformation', on_delete=models.CASCADE)
     
     
         
    def get_absolute_url(self):
        return reverse ("modalities", kwargs={"id":self.id})
    
    def get_modality_representation(self):
        return f"{self.title}, {self.description} [{self.ae_title}]"  