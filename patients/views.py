from operator import attrgetter
from datetime import datetime
from django.shortcuts import (
    render, get_object_or_404, redirect)
from django.urls import reverse
from .models import PatientInformation
from .forms import PatientInformationForm
from django.db.models import Q
from django.views.generic import DetailView
from django.views import View
from curaMED import helpers


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
    
    for patient in queryset:
        curamed_patient_id = patient.id
        patient.studies = []
        orthanc_patient_id = helpers.orthanc.get_orthanc_id(curamed_patient_id)
        studies_response, status = helpers.orthanc.get_request(f"/patients/{orthanc_patient_id}")
        
        if not studies_response:
            continue
        for orthanc_study_id in studies_response.get("Studies", []):
            study_response, status = helpers.orthanc.get_request(f"/studies/{orthanc_study_id}")
            study_date = study_response.get("MainDicomTags",{}).get("StudyDate","")
            study_time = study_response.get("MainDicomTags",{}).get("StudyTime","")
            try:
                nice_date_time = datetime.strptime(study_date + "-" + study_time, "%Y%m%d-%H%M%S")
            except ValueError:
                study_date, study_time = "",""
            else:
                study_date = nice_date_time.strftime("%d. %B %Y")
                study_time = nice_date_time.strftime("%H:%M")
            study_description = study_response.get("MainDicomTags",{}).get("StudyDescription","") 
            patient.studies.append({"study_date": study_date,
                                    "study_time": study_time,
                                    "study_description": study_description,
                                    "study_id": orthanc_study_id})
    
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

 