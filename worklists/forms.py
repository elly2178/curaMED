from django import forms 
from.models import WorklistInformation
from modalities.models import ModalitiesInformation
from modalities.models import ModalityModelChoiceField
from patients.models import PatientInformation
 
class WorklistInformationForm(forms.ModelForm):
    scheduled_procedure_step_start_date = forms.CharField(label='Auftragsdatum') 
    scheduled_procedure_step_start_time  = forms.CharField(label='Auftragszeit')
    modality = ModalityModelChoiceField(
        queryset=ModalitiesInformation.objects.all(), 
        to_field_name='ae_title', 
        initial=0)   
    doctor_list = [('dr1', 'Dr. Thomas Buerkle'), ('dr2','Dr. Michael Lehmann'),('dr3', 'Dr. Stephan Nuessli')]
    scheduled_performing_physician_s_name = forms.ChoiceField(choices=doctor_list,label='Zuständiger Arzt')
    patient_s_name = forms.CharField()
    patient_id = forms.CharField(required = False,label='Patient ID')
    patient_s_birth_date = forms.CharField(required = False,label='Patient Geburtstag') 
    patient_s_sex = forms.CharField(required = False, label='Patient Geschlecht')
    scheduled_procedure_step_description =  forms.CharField(required = False, label='Auftragsdeskription')
   
    class Meta: 
        model = WorklistInformation
        fields = [ 
            'scheduled_procedure_step_start_date',
            'scheduled_procedure_step_start_time',
            'modality',
            'scheduled_performing_physician_s_name',
            'patient_s_name',
            'patient_id',
            'patient_s_birth_date',
            'patient_s_sex',
            'scheduled_procedure_step_description'
        ]
        
    

 