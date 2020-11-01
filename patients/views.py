
from django.shortcuts import render, get_object_or_404, redirect
from .models import PatientInformation
from .forms import PatientInformationForm



# Create your views here.
def patient_list_view(request):
    queryset = PatientInformation.objects.all()
    context ={
        'object_list': queryset
    }
    return render(request, 'patient/patient_list.html', context)
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
        'form':form
    }
    return render(request, 'patient/create.html', context)
 