from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import ModalitiesInformation
from .forms import ModalitiesInformationForm
from administration.models import AdministrationInformation
from django.core.exceptions import ValidationError


from django.contrib import messages

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
    ip = request.GET.get('ip-address')
    port = request.GET.get('port-address')
    aetitle = request.GET.get('ae-title')
    location = request.GET.get('location-id')
    bad_parameters = []
    if not ip:
        bad_parameters.append("IP Address")
    if not port:
        bad_parameters.append("Port")
    if not aetitle:
        bad_parameters.append("AETitle")
    if not location:
        bad_parameters.append("Standort")
    if bad_parameters:
        return HttpResponse(status=400, reason=f"Ungültig: {', '.join(bad_parameters)}")
    
    import time
    time.sleep(3)
    return HttpResponse(status=200, reason=f"Modalität gefunden")
             
    #Client (clicks on Verbindungstest) -> jQuery sendet Request zu curaMED mit Infos zu Standort der Modalität und IPAdresse und Port und AETitle
    #POST c0100-orthanc.curapacs.ch/locations/{location-id}/modalities/echo (body: {ipaddress: 10.1.43.5, port: 104, aetitle: PHILIPSFUBAR}