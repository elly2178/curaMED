from django import forms

from.models import PatientInformation
#from phonenumber_field.formfields import PhoneNumberField

class PatientInformationForm(forms.ModelForm):
    #change text to german here + in the models
    name = forms.CharField()
    vorname = forms.CharField()
    geburtsdatum = forms.DateField(
        widget=forms.DateInput(attrs={"placeholder": "Jahr-Monat-Tag"}))
    adresse = forms.CharField()
    plz = forms.CharField()
    sprache = forms.CharField(required=False)
    #telefon = PhoneNumberField()
    class Meta: 
        model = PatientInformation
        fields = [
            'title',
            'name',
            'vorname',
            'geburtsdatum',
            'adresse',
            'plz',
            'sprache'
            #'telefon'
        ]
