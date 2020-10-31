from django import forms

from.models import AdministrationInformation

class AdministrationInformationForm(forms.ModelForm):
    class Meta: 
        model = AdministrationInformation
        fields = [
             'street',
             'city',
             'plz',
             'number'
        ]
