from django.http import HttpResponse
from django.shortcuts import render
from .forms import ModalitiesInformationForm


# Create your views here.
def modality_create_view(request):
    form = ModalitiesInformationForm(request.POST or None)
    if form.is_valid():
        form.save()
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