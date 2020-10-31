from django import forms

from.models import AdministrationInformation

class AdministrationInformationForm(forms.ModelForm):
    strasse =  forms.CharField(
        widget=forms.TextInput(attrs=
    {"placeholder": "Mittlerestrasse"}))
    stadt =  forms.CharField(
        widget=forms.TextInput(attrs=
    {"placeholder": "Zürich"}))
    plz =  forms.CharField(
        widget=forms.TextInput(attrs=
    {"placeholder": "8000"}))
    nummer =  forms.CharField(
        widget=forms.TextInput(attrs=
    {"placeholder": "28"}))
    class Meta: 
        model = AdministrationInformation
        fields = [
             'street',
             'city',
             'plz',
             'number'
        ]
