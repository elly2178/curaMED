from django import forms

from.models import ModalitiesInformation

class ModalitiesInformationForm(forms.ModelForm):
    title =  forms.CharField(
        widget=forms.TextInput(attrs=
    {"placeholder": "Ultraschall"}))
    description = forms.CharField(required=False)
    status = forms.CharField(required=False)
    class Meta: 
        model = ModalitiesInformation
        fields = [
            'title',
            'description',
            'status'
        ]


 
    