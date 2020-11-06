
from django.shortcuts import render, get_object_or_404, redirect
from .models import PatientInformation
from .forms import PatientInformationForm



# Create your views here.
# asta e nou
def patient_update_view(request, id= id):
    obj = get_object_or_404(PatientInformation, id= id)
    form = PatientInformationForm(request.POST or None, instance =obj)
    if form.is_valid():
        form.save()
    context = {
        'form' : form
    }
    return render(request, 'patient/patient_create.html', context)
# asta e nou
def patietn_detail_view(request, id):
    obj = get_object_or_404(PatientInformation, id = id)
    context ={
        'object' : obj
    }
    return render(request, 'patient/patient_detail.html', context)

def patient_search_view(request):
    if request.method =='GET':
        search = request.GET.get('search')
        post = PatientInformation.objects.all().filter(id=search)
        context = {
            'post': post
        }
        return render(request, 'patient/patient_list.html', context )

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
    return render(request,'patient/patient_delete.html', context)

#similar cu create wl
def patient_create_view(request):
    form = PatientInformationForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PatientInformationForm()
    context = {
        'form':form
    }
    return render(request, 'patient/create.html', context)
 