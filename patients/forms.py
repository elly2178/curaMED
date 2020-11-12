from django import forms 
from.models import PatientInformation

#from phonenumber_field.formfields import PhoneNumberField
class DateInput(forms.DateInput):
    input_type = 'date'

class PatientInformationForm(forms.ModelForm):
    #change text to german here + in the models
    sex = [('male','Herr'),('female','Frau')]
    title = forms.ChoiceField(required = False, choices=sex , label='Geschlecht')
    first_name = forms.CharField(label='Nachname')
    second_name = forms.CharField(label='Vorname')
    birthdate = forms.DateField(widget=DateInput(),label='Geburtsdatum')
    address = forms.CharField(label='Addresse')
    number = forms.CharField(label='Nummer')
    code = forms.CharField(label='PLZ')
    language = forms.CharField(required=False, label='Sprache')
    #telefon = PhoneNumberField()
    
    class Meta: 
        model = PatientInformation
        fields = [
            'title',
            'first_name',
            'second_name',
            'birthdate',
            'address',
            'number',
            'code',
            'language'
            
            #'telefon'
        ]
        widgets = {}
    
