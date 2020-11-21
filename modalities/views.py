from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import ModalitiesInformation
from .forms import ModalitiesInformationForm
 

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
        #make the redirect to another page
        return redirect('modalities')
    
    context = {
        'object':obj
    }
    return render(request, 'modality/modality_delete.html', context)

def modality_create_view(request):
    form = ModalitiesInformationForm(request.POST or None)
    if form.is_valid():  
        messages.warning(request,'aeTitle existiert bereit in den Datenbank. Entweder existierende Modalität bearbeiten oder anderen AETitle eingeben')     
        form.save()
        form = ModalitiesInformationForm()        
        return redirect('modalities')
    
    
    context = {
        'form':form 
    }
    return render(request, 'modality/create.html', context)
   
 
def modality_detail_view(request,id):
    obj = ModalitiesInformation.objects.get(id=id)
    context = {
        'object':obj
    }
    return render(request, 'modality/detail.html', context)