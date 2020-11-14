from django import forms

from.models import AdministrationInformation

class AdministrationInformationForm(forms.ModelForm):
    
    name = forms.CharField(label='Betriebsname',
    widget=forms.TextInput(attrs=
    {"placeholder": "Praxis Brönnimann"}))
    street =  forms.CharField(label='Strasse',
        widget=forms.TextInput(attrs=
    {"placeholder": "Mittlerestrasse"}))
    number =  forms.CharField(label='Nr.',
        widget=forms.TextInput(attrs=
    {"placeholder": "28"}))
    city =  forms.CharField(label='Stadt',
        widget=forms.TextInput(attrs=
    {"placeholder": "Zürich"}))
    plz =  forms.CharField(label='PLZ',
        widget=forms.TextInput(attrs=
    {"placeholder": "8000"}))
    
    telefon_number = forms.CharField(label='Telefon Nr.',
    widget=forms.TextInput(attrs=
    {"placeholder": "123456789"}))
   
    class Meta: 
        model = AdministrationInformation
        fields = [
            'name',
             'street',
             'city',
             'plz',
             'number',
             'telefon_number',
        ]

