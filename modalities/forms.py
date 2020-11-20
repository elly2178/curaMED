from django import forms
from.models import ModalitiesInformation
from administration.models import AdministrationInformation
from administration.models import StandortModelChoiceField

class ModalitiesInformationForm(forms.ModelForm):
    # locations = [("fu","bar"),("fub","schmeow")] #AdministrationInformation.objects.all()
    # print("LOCATIONS is: " + str(locations))
    ae_title = forms.CharField(widget=forms.TextInput(attrs=
    {"placeholder": "aeXR05"}))
    title =  forms.CharField(
        widget=forms.TextInput(attrs=
    {"placeholder": "Ultraschall"}))
     
    description = forms.CharField(required=False, label="Beschreibung")
     
    # title --> dicmo ae title
    # mouse over --> help text for dicom ae title
    # make pretty
    # new button Verbindungstest
    # 
    
    ip = forms.GenericIPAddressField(label="IP Adresse")
    port = forms.CharField()
    associate_location = StandortModelChoiceField(
    label="Standort",queryset=AdministrationInformation.objects.all(), to_field_name='street', initial=0)

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


 
    