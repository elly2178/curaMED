from django import forms
from.models import ModalitiesInformation
from administration.models import AdministrationInformation
from administration.models import LocationModelChoiceField
from django.core.exceptions import ValidationError
 

class ModalitiesInformationForm(forms.ModelForm):
    ae_title = forms.CharField(widget=forms.TextInput(attrs=
    {"placeholder": "ae23456jdmglo_01"}))
    title =  forms.CharField(
        widget=forms.TextInput(attrs=
    {"placeholder": "Ultraschall"}))
    description = forms.CharField(required=False, label="Beschreibung")
     
    # mouse over --> help text for dicom ae title
    # new button Verbindungstest
    # 
    
    ip = forms.GenericIPAddressField(label="IP Adresse")
    port = forms.CharField()
    associate_location = LocationModelChoiceField(label="Standort",
                                                  queryset=AdministrationInformation.objects.all(),
                                                  to_field_name='id',
                                                  initial=0)


    def clean_ae_title(self):
        ae_title = self.cleaned_data['ae_title']
        if ModalitiesInformation.objects.filter(ae_title=ae_title).exists():
            raise ValidationError("Eine Modalität mit diesem AETitle existiert bereits.")
            
        return ae_title

    class Meta: 
        model = ModalitiesInformation
        fields = [
            'ae_title',
            'title',
            'description',
            'ip',
            'port',
            'associate_location'
        ]


 
    