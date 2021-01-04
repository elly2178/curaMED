from django import forms
from.models import ModalitiesInformation
from administration.models import AdministrationInformation
from administration.models import LocationModelChoiceField
from django.core.exceptions import ValidationError
 

class ModalitiesInformationForm(forms.ModelForm):
    types = [('CR','Computerradiografie'),
    ('CT','Computertomografie'),
    ('US','Ultraschall'),
    ('ES','Endoskopie'),
    ('DX','Digitale Radiografie'), 
    ('MG','Mammografie')    
    ]
    # more titles under: http://dicomlookup.com/modalities.asp
    ae_title = forms.CharField(
        widget=forms.TextInput(attrs={'class' : 'form-control', "placeholder": "MTX203"}))
  
    title =  forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                                choices=types, label='Typ')
     
    description = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}),
                                    required=False, label="Beschreibung")
    ip = forms.GenericIPAddressField(widget=forms.TextInput(attrs={'class' : 'form-control'}),
                                    label="IP Adresse")
    port = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control',"placeholder": "104"}))
    associate_location = LocationModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                                                    label="Standort",
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


 
    