from django import forms
from.models import ModalitiesInformation
from administration.models import AdministrationInformation
from administration.models import StandortModelChoiceField

class ModalitiesInformationForm(forms.ModelForm):
    # locations = [("fu","bar"),("fub","schmeow")] #AdministrationInformation.objects.all()
    # print("LOCATIONS is: " + str(locations))
    title =  forms.CharField(
        widget=forms.TextInput(attrs=
    {"placeholder": "Ultraschall"}))
     
    description = forms.CharField(required=False, label="Beschreibung")
    # status entfernen, 
    # title --> dicmo ae title
    # mouse over --> help text for dicom ae title
    # make pretty
    # new button Verbindungstest
    # 
    status = forms.CharField(required=False)
    ip = forms.GenericIPAddressField(label="IP Adresse")
    port = forms.CharField()
    associate_location = StandortModelChoiceField(label="Standort",queryset=AdministrationInformation.objects.all(), to_field_name='street')

    class Meta: 
        model = ModalitiesInformation
        fields = [
            'title',
            'description',
            'ip',
            'port',
            'status',
            'associate_location'
        ]


 
    