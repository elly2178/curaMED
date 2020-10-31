
from django.shortcuts import render
from .models import PatientInformation
from .forms import PatientInformationForm


# Create your views here.
def patient_create_view(request):
    form = PatientInformationForm(request.POST or None)
    if form.is_valid():
        form.save()
        
    context = {
        'form':form
    }
    return render(request, 'patient/create.html', context)

def patient_detail_view(request):
    obj = PatientInformation.objects.get(id=2)
    context = {
        'object':obj
    }
    return render(request, 'patient/detail.html', context)

 