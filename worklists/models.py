from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime
from modalities.models import ModalitiesInformation
# Create your models here.
class WorklistInformation(models.Model):
    # schedules_station_ae_title = this is a dropdown. needs tp be unique
    # ae title MUSS unique sein. keine Ü Ä Ö
    #scheduled_station_ae_title = models.ForeignKey('modalities.ModalitiesInformation', on_delete=models.CASCADE)
     
    scheduled_procedure_step_start_date = models.CharField(max_length=100)
    scheduled_procedure_step_start_time = models.CharField(max_length=12)

    modality = models.ForeignKey('modalities.ModalitiesInformation', on_delete=models.CASCADE)

    doctor_list = [('dr1', 'Dr. Thomas Bürkle'), ('dr2','Dr. Michael Lehmann'),('dr3', 'Dr. Stephan Nüssli')]
    scheduled_performing_physician_s_name = models.CharField(max_length=80,choices=doctor_list)
    #scheduled_performing_physician_s_name = models.CharField(max_length=80)

    patient_s_name = models.CharField(max_length=100) 
    patient_id = models.CharField(max_length= 64) 
    
    patient_s_birth_date = models.CharField(max_length=100) 
    patient_s_sex = models.CharField(max_length=4)
    
    scheduled_procedure_step_description =  models.CharField(max_length=64)
    def get_absolute_url(self):
        return reverse("worklists", kwargs={"id":self.id})