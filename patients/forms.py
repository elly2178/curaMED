from django import forms 
from.models import PatientInformation
import datetime
 

class DateInput(forms.DateInput):
    input_type = 'date'
  

class PatientInformationForm(forms.ModelForm):
    
    sex = [('male','Herr'),('female','Frau')]
    title = forms.ChoiceField(required = False, choices=sex , label='Geschlecht')
    first_name = forms.CharField(label='Nachname')
    second_name = forms.CharField(label='Vorname')
      

    birthdate = forms.DateField( 
    widget=DateInput(  ) , label='Geburtsdatum')
    address = forms.CharField(label='Addresse')
    number = forms.CharField(label='Nummer')
    city = forms.CharField(label='Stadt')
    code = forms.CharField(label='PLZ')
    language = forms.CharField(required=False, label='Sprache')
        
    class Meta: 
        model = PatientInformation
        fields = [
            'title',
            'first_name',
            'second_name',
            'birthdate',
            'address',
            'number',
            'city',
            'code',
            'language'
            ]
        widgets = {}
    
