from django.shortcuts import render
from .models import WorklistInformation
from patients.models import PatientInformation
from .forms import WorklistInformationForm
from django.views import View
from django.shortcuts import (render, get_object_or_404, redirect)
from datetime import datetime,date
import json
import requests
from curaMED import helpers

class WorklistCreateView(View):
    template_name = 'worklists/worklist_create.html'
    def get(self, request, *args, **kwargs):
        patient_id = request.GET.get('patient-id')
        patient = get_object_or_404(PatientInformation, id=patient_id)
        form = WorklistInformationForm(request.POST)
        current_date = date.today()
        print("YOUR DATE IS: " + str(current_date))
        current_time = datetime.today()       
        context = {
            'time': current_time,
            'date':current_date, 
            'patient': patient,
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):        
        form = WorklistInformationForm(request.POST)
        if form.is_valid():
            form.save() 
            data_dict = create_curapacs_worklist_request(form.cleaned_data)
            #add error handling
            response = requests.post(helpers.orthanc.get_url_for_path("worklists"),
                                     json=data_dict,
                                     auth=(helpers.orthanc.username, helpers.orthanc.password))
            print("Response was: " + str(response.status_code))
            return redirect('patients')
        print("FORM ERRORS: " + str(form.errors))
        context = {'form':form}
        return render(request, self.template_name, context)

def get_doctors_name(some_short_name):
    for short_name, long_name in WorklistInformation.doctor_list:
        if some_short_name == short_name:
            return long_name
    raise ValueError(f"Doctor for {some_short_name} not found.")

def create_curapacs_worklist_request(form_cleaned_data):
    physician_name = get_doctors_name(form_cleaned_data.get("scheduled_performing_physician_s_name"))
    physician_name = physician_name.replace(" ", "^")
    worklist_datetime = datetime.strptime(f"{form_cleaned_data.get('scheduled_procedure_step_start_date')}\
         {form_cleaned_data.get('scheduled_procedure_step_start_time')}", "%d. %B %Y %H:%M")
    return {
        "PatientID": form_cleaned_data.get("patient_id"),
        "PatientName": form_cleaned_data.get("patient_s_name").replace(" ","^"),
        "ScheduledProcedureStepSequence": [
            {
                "Modality": str(form_cleaned_data.get("modality").title),
                "ScheduledStationAETitle": str(form_cleaned_data.get("modality").ae_title),
                "ScheduledProcedureStepStartDate": worklist_datetime.strftime("%Y%m%d"), 
                "ScheduledProcedureStepStartTime": worklist_datetime.strftime("%H%M%S"),
                "ScheduledPerformingPhysicianName": physician_name
            }
        ]
        }

def worklist_list_view(request):
    queryset = WorklistInformation.objects.all()
    context ={
        'object_list': queryset        
    }
    return render(request, 'worklists/worklist_list.html', context)