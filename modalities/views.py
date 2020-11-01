from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import ModalitiesInformation
from .forms import ModalitiesInformationForm


# Create your views here.
def modality_delete_view(request,id):
    obj = get_object_or_404(ModalitiesInformation, id=id)
    if request.method =='POST':
        obj.delete()
        #make the redirect to another page
        return redirect('../../')
    
    context = {
        'object':obj
    }
    return render(request, 'modality/modality_delete.html', context)

def modality_create_view(request):
    form = ModalitiesInformationForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ModalitiesInformationForm()
    context = {
        'form':form
    }
    return render(request, 'modality/create.html', context)
 
def modality_detail_view(request):
    obj = ModalitiesInformation.objects.get(id=2)
    context = {
        'object':obj
    }
    return render(request, 'modality/detail.html', context)