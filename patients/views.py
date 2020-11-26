from operator import attrgetter

from django.shortcuts import (
    render, get_object_or_404, redirect)
from django.urls import reverse
from .models import PatientInformation
from .forms import PatientInformationForm
from django.db.models import Q
from django.views.generic import DetailView

from django.views import View

def patient_update_view(request, id= id):
    obj = get_object_or_404(PatientInformation, id= id)
    form = PatientInformationForm(request.POST or None, instance =obj)
    if form.is_valid():
        form.save()
    context = {
        'form' : form
    }
    return render(request, 'patient/patient_create.html', context)


def patient_detail_view(request, id):
    obj = get_object_or_404(PatientInformation, id=id)
    form = PatientInformationForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        form = PatientInformationForm()
        return redirect('patients')
    else:
        if request.POST:
            del form.errors["title"]
            del form.errors["birthdate"]
            form.save()
            form = PatientInformationForm()
            return redirect('patients')
    context = {
        'object': obj
    }
    return render(request, 'patient/patient_detail.html', context)

def patient_search_view(query=None):    
    queryset= []
    queries = []
    if query is not None:
        queries = query.split(' ')
    
    for q in queries:
        patients = PatientInformation.objects.filter(
            Q(first_name__icontains=q)|         
            Q(second_name__icontains=q)
        ).distinct()
        for patient in patients:
            queryset.append(patient)
    return list(set(queryset)) 

def patient_search_result_view(request):
    context = {}
    query = ''
    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)
    patient = sorted(patient_search_view(query), key=attrgetter('id'), reverse=True)
    context['object_list'] = patient
    return render(request, 'patient/patient_list.html', context)
 
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
        return redirect('patients')
    context = {
        'object':obj
    }
    return render(request,'patient/patient_delete.html', context)


class PatientCreateView(View):
    template_name = 'patient/patient_create.html'
    def get(self, request, *args, **kwargs):
        # get method
        form = PatientInformationForm()
        context = {
            'form':form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        #post method 
        form = PatientInformationForm(request.POST)
        print(str(form))
        if form.is_valid():
            form.save()
            return redirect('patients')
        context = { 'form':form }
        return render(request, self.template_name, context)