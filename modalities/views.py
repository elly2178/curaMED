from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import ModalitiesInformation
from .forms import ModalitiesInformationForm
from administration.models import AdministrationInformation

from django.contrib import messages

def modality_list_view(request):
    
    queryset = ModalitiesInformation.objects.all()
     
    context ={
        'object_list': queryset
    }
    print("QUERYSET IS " + str(queryset) + " including: location "+ str(queryset[0].associate_location.street))
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
    # editing modality does not work
    obj = ModalitiesInformation.objects.get(id=id)
    context = {
        'object':obj
    }
    return render(request, 'modality/detail.html', context)