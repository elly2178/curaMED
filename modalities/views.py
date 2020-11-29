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