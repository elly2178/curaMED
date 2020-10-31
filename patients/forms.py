from django import forms

from.models import PatientInformation

class PatientInformationForm(forms.ModelForm):
    class Meta: 
        model = PatientInformation
        fields = [
            'title',
            'first_name',
            'second_name',
            'birthdate',
            'language'
        ]