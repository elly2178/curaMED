from django import forms

from.models import PatientInformation

class PatientInformationForm(forms.ModelForm):
    #change text to german here + in the models
    first_name = forms.CharField()
    second_name = forms.CharField()
    geburtstag = forms.DateField(
        widget=forms.DateInput(attrs={"placeholder": "Jahr-Monat-Tag"}))
    sprache = forms.CharField(required=False)
    class Meta: 
        model = PatientInformation
        fields = [
            'title',
            'first_name',
            'second_name',
            'geburtstag',
            'sprache'
        ]
