from django import forms

from.models import PatientInformation

#from phonenumber_field.formfields import PhoneNumberField

class PatientInformationForm(forms.ModelForm):
    #change text to german here + in the models
    sex=[('male','Herr'),('female','Frau')]
    title = forms.ChoiceField(choices = sex, label='Geschlecht')
    first_name = forms.CharField(label='Nachname')
    second_name = forms.CharField(label='Vorname')
    birthdate = forms.DateField(label='Geburtsdatum',
        widget=forms.DateInput(attrs={"placeholder": "Jahr-Monat-Tag"}))
    address = forms.CharField(label='Addresse')
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
            'code',
            'language'
            #'telefon'
        ]
