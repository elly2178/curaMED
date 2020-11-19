from django import forms 
from.models import WorklistInformation
from modalities.models import ModalitiesInformation
from modalities.models import ModalityModelChoiceField
from patients.models import PatientInformation
# from patients.models import PatientModelChoiceField


# class DateInput(forms.DateInput):
#     input_type = 'date'

class WorklistInformationForm(forms.ModelForm):
    # scheduled_station_ae_title = StandortModelChoiceField(label='ae title',
    # queryset=WorklistInformation.objects.all(), to_field_name='street')

    #change text to german here + in the models
    scheduled_procedure_step_start_date = forms.CharField(label='Auftragsdatum') 
    # nicht field sondern calendar/ time whaterver
    # yetzige time
    scheduled_procedure_step_start_time  = forms.CharField(label='Auftragszeit')
    modality = ModalityModelChoiceField(
        queryset=ModalitiesInformation.objects.all(), to_field_name='ae_title')
    # modality als doropdpwn
    scheduled_performing_physician_s_name = forms.CharField(label='Zuständiger Arzt')
    # doctor automatisch reigefügr, pat id should unedit + name
    patient_s_name = forms.CharField()
    # patient_s_name =  PatientModelChoiceField(label='Patienten name',
    #     queryset=PatientInformation.objects.all(), to_field_name='first_name')
    
    patient_id = forms.CharField(label='Patient ID')
    # description als textfield
    patient_s_birth_date = forms.CharField(required = False,label='Patient Geburtstag') 
    patient_s_sex = forms.CharField(required = False, label='Patient Geschlecht')
    scheduled_procedure_step_description =  forms.CharField(required = False, label='Auftragsdeskription')
    

    
    
    class Meta: 
        model = WorklistInformation
        fields = [
            #'scheduled_station_ae_title',
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
        #widgets = {}
    

 