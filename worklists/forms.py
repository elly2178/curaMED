 from django import forms 
from.models import WorklistInformation

 
class DateInput(forms.DateInput):
    input_type = 'date'

class PatientInformationForm(forms.ModelForm):
    #change text to german here + in the models
    scheduled_procedure_step_start_date = forms.CharField() 
    scheduled_procedure_step_start_time  = forms.CharField()
    modality = forms.CharField()
    scheduled_performing_physician_s_name = forms.CharField()
    patient_s_name = forms.CharField()
    patient_id = forms.CharField()
    scheduled_procedure_step_description =  forms.CharField(required = False)
    patient_s_birth_date = forms.CharField(required = False) 
    patient_s_sex = forms.CharField(required = False)
    
    class Meta: 
        model = WorklistInformation
        fields = [
            'scheduled_procedure_step_start_date',
            'scheduled_procedure_step_start_time',
            'modality',
            'scheduled_performing_physician_s_name',
            'patient_s_name',
            'patient_id',
            'scheduled_procedure_step_description',
            'patient_s_birth_date',
            'patient_s_sex'
             
        ]
        #widgets = {}
    

 