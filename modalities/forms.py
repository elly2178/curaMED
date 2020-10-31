from django import forms

from.models import ModalitiesInformation

class ModalitiesInformationForm(forms.ModelForm):
    class Meta: 
        model = ModalitiesInformation
        fields = [
            'title',
            'description',
            'status'
        ]