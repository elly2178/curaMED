from operator import attrgetter
from datetime import datetime
from django.shortcuts import (render, get_object_or_404, redirect)
from django.urls import reverse
from .models import PatientInformation
from .forms import PatientInformationForm
from django.db.models import Q
from django.views.generic import DetailView
from django.views import View
from curaMED import helpers
import requests
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponseServerError
import json

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
            study_instance_uid = study_response.get("MainDicomTags",{}).get("StudyInstanceUID", "")
            study_description = study_response.get("MainDicomTags",{}).get("StudyDescription","") 
            if study_description == "curaPACS Patient Import":
                continue
            study_date = study_response.get("MainDicomTags",{}).get("StudyDate","")     
            study_time = study_response.get("MainDicomTags",{}).get("StudyTime","")
            try:
                nice_date_time = datetime.strptime(study_date + "-" + study_time, "%Y%m%d-%H%M%S")
            except ValueError:
                study_date, study_time = "",""
            else:
                study_date = nice_date_time.strftime("%d. %B %Y")
                study_time = nice_date_time.strftime("%H:%M")            
            patient.studies.append({"study_date": study_date,
                                    "study_time": study_time,
                                    "study_description": study_description,
                                    "study_id": orthanc_study_id,
                                    "study_instance_uid": study_instance_uid})
    
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

def patient_import_view(request):    
    if request.method == "POST":
        try:
            patient_ids_to_be_imported = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponseBadRequest(f"Failed to decode request")
        http_response = import_patients_in_curapacs(patient_ids_to_be_imported)
        return http_response

    queryset = PatientInformation.objects.all() 
    patients_to_be_imported = []
    for patient in queryset:
        curamed_patient_id = patient.id
        orthanc_patient_id = helpers.orthanc.get_orthanc_id(curamed_patient_id)
        patient_response, status_code = helpers.orthanc.get_request(f"/patients/{orthanc_patient_id}")
        if status_code == 404:
            patients_to_be_imported.append(patient)
        else:
            continue
    context ={
        'object_list': patients_to_be_imported
    }
    return render(request, 'patient/patient_import.html', context)

def import_patients_in_curapacs(patient_ids):
    print(f"Gathering queryset for patients with ids {[int(patient_id) for patient_id in patient_ids]}")
    queryset = PatientInformation.objects.filter(pk__in=[int(patient_id) for patient_id in patient_ids])
    request_body = []
    for patient in queryset:
        request_body.append({"id": str(patient.id),
                             "first_name": patient.first_name,
                             "last_name": patient.second_name,
                             "sex": patient.title,
                             "birthdate": patient.birthdate.strftime("%Y-%m-%d")
                             })
    try:
        print(f"POSTING TO /import-patients: {request_body}")
        response_dict, response_status = helpers.orthanc.post_request(f"/import-patients",
                                                                      request_body,
                                                                      timeout=12)
    except ValueError as err:
        return HttpResponseServerError(f"Import failed: {err}")
    if response_status != 200:
        return HttpResponseBadRequest(f"Import failed ({response_status}): {response_dict}")

    print(f"Response dict is: {response_dict}")
    imported_patients = response_dict.get("content",{}).get("imported")
    failed_patients = response_dict.get("content",{}).get("failed")
    
    results_dict = {"imported": imported_patients, "failed": failed_patients}
    #if response_dict.get("status") == "success":
    return HttpResponse(content=json.dumps(results_dict), content_type="application/json")  
    #check the response
    #if response body contains "status": "success":
    # body "content" key contains "imported" key, value is list of patient_ids which where successfully imported
    #else response body contains "status": "error":
    # body "content" key contains "imported" key, value is list of patient_ids which where successfully imported
    # body "content" key contains "failed" key, value is list of patient_ids which where not imported successfully
    #  --> return HttpResponse()

def fetch_meddream_token(request):
    #Take the request from the django user
    #Find out which study the django user wants to access
    #We do this by parsing the query string of the GET request sent by our users
    #the query string contains a key called "study-instanc-uid" which contains the dicom study id 
    # that the users want to access
    #
    if not request.method == 'GET':
        return HttpResponseNotAllowed(('GET',))    

    study_instance_uid = request.GET.get('study-instance-uid')
    if study_instance_uid is None:
        return HttpResponseBadRequest(content="Missing query string key and value for study-instance-uid")

    body = { "items": [
            {"studies": {
                "study": study_instance_uid,
                "storage": "Orthanc"}
            } ]
            }       
    try:
        response_dict, response_status = helpers.orthanc.post_request("/generate-meddream-token", body)
    except ValueError as err:
        return HttpResponseServerError(content=f"Failed to fetch Token from Token Service: {err}")

    if response_dict.get("status") == "success":
        return redirect(f"https://c0100-meddream.curapacs.ch/?token={response_dict.get('content')}&add=true")
    else:
        return HttpResponseBadRequest(content="Failed beacause {response_dict.get('reason')}")

def do_patient_merge(original_dicom_patient_uid: str, duplicate_dicom_patient_uids: list):
    original_dicom_patient_orthanc_uid = helpers.orthanc.get_orthanc_id(original_dicom_patient_uid)
    duplicate_orthanc_patient_uids = []
    for uid in duplicate_dicom_patient_uids:
        duplicate_orthanc_patient_uids.append(helpers.orthanc.get_orthanc_id(uid))
    body = duplicate_orthanc_patient_uids
    try:
        response_dict, response_status = helpers.orthanc.post_request(f"/merge-patients/{original_dicom_patient_orthanc_uid}", body)
    except ValueError as err:
        return HttpResponseServerError(content=f"Failed to merge patients: {err}")
    if response_status == 200:
        merge_status = response_dict.get("status")
        if merge_status == "error":
            print(f"Merge failed, reason {response_dict.get('reason')}: {response_dict.get('content')}")
        return HttpResponse(content=json.dumps(response_dict.get("content")))
    else:
        return HttpResponse(content=json.dumps({"merged": [], "failed": duplicate_dicom_patient_uids}))

def patient_merge_view(request,id):
    if request.method == "POST":
        #return HttpResponse(content=json.dumps({"merged": [], "failed": ["3","4"]}))
        try:
            duplicate_dicom_patient_uids = json.loads(request.body)            
        except json.JSONDecodeError:
            return HttpResponseBadRequest(f"Failed to decode request")
        http_response = do_patient_merge(id, duplicate_dicom_patient_uids)
        return http_response

    obj = PatientInformation.objects.get(id=id)
    
    context = {
        "object": obj
    }
    return render(request, 'patient/patient_merge.html', context)

def curapacs_search_patients_view(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(('GET',))
    patient_id_query = str(request.GET.get("patient-id", "*"))
    patient_name_query = str(request.GET.get("patient-name", "*"))
    max_results_count = request.GET.get("max-results-count", 10)
    if patient_id_query is None and patient_name_query is None:
        return HttpResponseBadRequest(f"Need at least patient-id or patient-name")
    
    request_body = {"Level": "Patient",
                    "Limit": max_results_count,
                    "Query": {                           
                        "PatientID": patient_id_query,
                        "PatientName": patient_name_query
                        }
                    }
    try:
        curapacs_search_response, status_code = helpers.orthanc.post_request(f"/tools/find",
                                                                             request_body,
                                                                             timeout=12)
    except ValueError:
        return HttpResponseServerError(f"Failed to connect to curaPACS")
    if status_code != 200:
        return HttpResponseServerError(f"curaPACS failed to handle search request ({status_code})")
    
    results_list = []
    for orthanc_uid in curapacs_search_response:        
        patient_information_response, status_code = helpers.orthanc.get_request(f"/patients/{orthanc_uid}")
        given_patient_id = patient_information_response.get("MainDicomTags",{}).get("PatientID","") 
        given_patient_name = patient_information_response.get("MainDicomTags",{}).get("PatientName","")  
        existing_patient_study_uids = patient_information_response.get("Studies",[])
        study_uids_nr = len(existing_patient_study_uids)
        results_list.append({"id": given_patient_id,
                             "name": given_patient_name,
                             "study_count": study_uids_nr
                             })        
    
    return HttpResponse(content=json.dumps(results_list), content_type="application/json")


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
        if form.is_valid():
            form.save()
            return redirect('patients')
        context = { 'form':form }
        return render(request, self.template_name, context)
