from django.db import models
from django.urls import reverse
from django.utils import timezone
from datetime import datetime
from modalities.models import ModalitiesInformation
from django.core.exceptions import ValidationError

def validate_date(somedate):
    import locale
    print("DATE BEFORE VALIDATION IS:" + str(somedate) + " locale is " + str(locale.getlocale()) + " default locale is " + str(locale.getdefaultlocale()) )
    #for fmt in ["%d. %B %Y", "%d-%m-%Y", "%Y-%m-%d"]
    try:
        retval = datetime.strptime(somedate, "%d. %B %Y")
    except ValueError:
        raise ValidationError("Datumsangabe nicht valide.")
    return retval

def validate_time(sometime):
    try:
        retval = datetime.strptime(sometime, "%H:%M")
    except ValidationError:
        raise ValidationError("Zeitangabe nicht valide.")
    return retval
        
class WorklistInformation(models.Model):
    scheduled_procedure_step_start_date = models.CharField(max_length=100, validators=[validate_date])
    scheduled_procedure_step_start_time = models.CharField(max_length=12, validators=[validate_time])
    modality = models.ForeignKey('modalities.ModalitiesInformation', on_delete=models.CASCADE)
    doctor_list = [('dr1', 'Dr. Thomas Burkle'), 
                    ('dr2','Dr. Michael Lehmann'),
                    ('dr3', 'Dr. Stephan Nuessli')]
    scheduled_performing_physician_s_name = models.CharField(max_length=80,choices=doctor_list)
    patient_s_name = models.CharField(max_length=100) 
    patient_id = models.CharField(max_length= 64)     
    patient_s_birth_date = models.CharField(max_length=100) 
    patient_s_sex = models.CharField(max_length=4)    
    scheduled_procedure_step_description =  models.CharField(max_length=64)
    
    def get_absolute_url(self):
        return reverse("worklists", kwargs={"id":self.id})