
from django.shortcuts import render, get_object_or_404, redirect
from .models import PatientInformation
from .forms import PatientInformationForm

#for translation
from django.utils.translation import gettext as _

# Create your views here.
def patient_delete_view(request,id):
    obj = get_object_or_404(PatientInformation, id=id)
    if request.method =='POST':
        obj.delete()
        #make the redirect to another page
        return redirect('../../')
    
    context = {
        'object':obj
    }
    return render(request, 'patient/patient_delete.html', context)

def patient_create_view(request):
    form = PatientInformationForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PatientInformationForm()
    context = {
        'form':_(form)
    }
    return render(request, 'patient/create.html', context)

def patient_detail_view(request):
    obj = PatientInformation.objects.get(id=2)
    context = {
        'object':obj
    }
    return render(request, 'patient/detail.html', context)

 