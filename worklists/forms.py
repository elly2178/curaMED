from django import forms 
from.models import WorklistInformation
from worklists.models import WorklistInformation
#from administration.models import StandortModelChoiceField
 
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
    modality = forms.CharField(label='Modalität')
    # modality als doropdpwn
    scheduled_performing_physician_s_name = forms.CharField(label='Zuständiger Arzt')
    # doctor automatisch reigefügr, pat id should unedit + name
    patient_s_name = forms.CharField(label='Patient Name')
    patient_id = forms.CharField(label='Patient ID')
    # description als textfield
    patient_s_birth_date = forms.CharField(required = False,label='Patient Geburtstag') 
    patient_s_sex = forms.CharField(required = False, label='Patient Geschlächt')
    scheduled_procedure_step_description =  forms.CharField(required = False, label='Auftragsdeskription')
    

    # associate_location = StandortModelChoiceField(
    # label="Standort",queryset=AdministrationInformation.objects.all(), to_field_name='street')
    # add button bestätigen + abbrechen 
    
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
    

 