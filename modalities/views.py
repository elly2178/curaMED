from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import ModalitiesInformation
from .forms import ModalitiesInformationForm
from administration.models import AdministrationInformation
from django.core.exceptions import ValidationError


from django.contrib import messages 
from curaMED import helpers
import json

def modality_list_view(request):
    queryset = ModalitiesInformation.objects.all()
    context ={
        'object_list': queryset
    }
    return render(request, 'modality/modality_list.html', context)

def modality_delete_view(request,id):
    obj = get_object_or_404(ModalitiesInformation, id=id)
    if request.method =='POST':
        obj.delete()
        return redirect('modalities')
    context = {
        'object':obj
    }
    return render(request, 'modality/modality_delete.html', context)

def modality_create_view(request):
    #oh, the user jst wants a connetion test (because the "action" attribute is set to Verbindungstest)
    #lets cann helpers.orthanc.post(/locations/{location-id}/modalities/echo)
    form = ModalitiesInformationForm(request.POST or None)
    if form.is_valid():        
        form.save()
        form = ModalitiesInformationForm()        
        return redirect('modalities')
    else:
        for fieldname, errormessages in form.errors.items():
            for errormessage in errormessages:
                messages.warning(request, errormessage) 
    context = {
        'form':form 
    }
    return render(request, 'modality/create.html', context)
 
def modality_detail_view(request,id): 
    obj = ModalitiesInformation.objects.get(id=id)
    dropdown = AdministrationInformation.objects.all()
    form = ModalitiesInformationForm(request.POST or None, instance=obj)
    if form.is_valid():        
        form.save()
        form = ModalitiesInformationForm()        
        return redirect('modalities')
    else:
        if request.POST:
            try:
                print("you are in the try", str(form))
                form.clean_ae_title()
            except (ValidationError, KeyError):
                del form.errors["ae_title"]
                form.save()
                form = ModalitiesInformationForm()    
                return redirect('modalities')
    context = {
        'form':form,
        'AdministrationInformation':dropdown,
        'object':obj
    }
    return render(request, 'modality/detail.html', context)

def modality_connection_test_view(request):
    #add here the post request from the helpers
    #checks if the user has inputted the fields
    # makes a post request at the url "https://c0100-orthanc.curapacs.ch/locations/0/echo" with the inputted fields that the user typed in
     
    if request.method == 'POST':        
        request_body = json.loads(request.body)       
        ip_address = request_body.get("ip_address")
        port = request_body.get("port")
        location = request_body.get("location_id")
        bad_parameters = []
        if not ip_address:
            bad_parameters.append("IP Address")
        if not port:
            bad_parameters.append("Port")
        if not location:
            bad_parameters.append("Standort")
        if bad_parameters:
            return HttpResponse(status=400, reason=f"Ungültig: {', '.join(bad_parameters)}")

        response_dict, response_status = helpers.orthanc.post_request(f"/locations/{location}/echo",
                                                                      request_body,
                                                                      timeout=10)
        return HttpResponse(content=json.dumps(response_dict),
                            content_type="application/json")         
    else:
        return HttpResponse(status=405,
                            content=json.dumps({'error': 'Methode nicht unterstützt'}),
                            content_type="application/json")
    