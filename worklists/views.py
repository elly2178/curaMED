from django.shortcuts import render
from .models import WorklistInformation
from patients.models import PatientInformation
from .forms import WorklistInformationForm
from django.views import View
from django.shortcuts import (render, get_object_or_404, redirect)
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError
from datetime import datetime,date
import json
import requests
from administration.models import AdministrationInformation
from modalities.models import ModalitiesInformation
from curaMED import helpers

class WorklistCreateView(View):
    template_name = 'worklists/worklist_create.html'
    def get(self, request, *args, **kwargs):
        patient_id = request.GET.get('patient-id')
        patient = get_object_or_404(PatientInformation, id=patient_id)
        form = WorklistInformationForm(request.POST)
        current_date = date.today()
        
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
            location_id = form.cleaned_data.get("modality").associate_location.id
            print(f"Doing POST at path " + helpers.orthanc.get_url_for_path(f'locations/{location_id}/worklists') + f" with body {data_dict}")
            try:
                response, status_code = helpers.orthanc.post_request(f"/locations/{location_id}/worklists/",
                                                                 data_dict,
                                                                 timeout=5)
            except ValueError as err:
                print("RETURNING SERVER ERROR")
                return HttpResponse(json.dumps({"status": "error","reason": "Location not found"}),
                                    content_type="application/json")
            print("Response was: " + str(status_code) + "  " +str(response))
            return HttpResponse(json.dumps(response), content_type="application/json")
        print("FORM ERRORS: " + str(form.errors))
        return HttpResponseBadRequest({"status": "error", "reason": str(form.errors)})

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
    worklist_dict = {
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
    return worklist_dict

def get_curapacs_worklists_by_location_request(request, location_id):
    """
    Takes a request including a location_id and queries curapacs with a GET at /locations/{location_id}/worklists
    Args:
        request (request): django request object
    """
    try:
        worklists_response, status_code = helpers.orthanc.get_request(f"/locations/{location_id}/worklists")
    except ValueError:
        worklists_response = {"status": "error"}
    return HttpResponse(content=json.dumps(worklists_response), content_type="application/json")

def get_curapacs_statistics(request, accession_number):   
    statistics_response, status_code = helpers.orthanc.get_request(f"/study-by-accession-number/{accession_number}/statistics")
    print(f"Got statistics response {str(statistics_response)[:30]} with status {status_code}")
    return HttpResponse(content=json.dumps(statistics_response), content_type="application/json")

def worklist_list_view(request):
    # form = WorklistInformationForm(request.GET)
    # location_id = form.cleaned_data.get("modality").associate_location.id
    queryset = AdministrationInformation.objects.all()
    queryModalitySet = ModalitiesInformation.objects.all()
    queryWorklistSet = WorklistInformation.objects.all()
    context ={
        'location_list': queryset,
        'modality_list': queryModalitySet,
        'worklist_list': queryWorklistSet        
    }
    return render(request, 'worklists/worklist_list.html', context)