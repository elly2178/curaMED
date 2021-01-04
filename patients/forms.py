from django import forms 
from.models import PatientInformation
import datetime
 

class DateInput(forms.DateInput):
    input_type = 'date'
    

class PatientInformationForm(forms.ModelForm):
    
    sex = [('male','Herr'),('female','Frau')]
    title = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                            required = False, choices=sex , label='Geschlecht')
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'})
                            ,label='Nachname')
    second_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}),
                            label='Vorname') 
    
    birthdate = forms.DateField(widget=DateInput(attrs={'class': 'form-control'}) ,label='Geburtsdatum')
    address = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}),
                                label='Addresse')
    number = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}),
                                label='Nummer')
    city = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}),
                            label='Stadt')
    code = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}),
                            label='PLZ')
    language = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}),
                        required=False, label='Sprache')
       
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
        widgets = { }
    
