from django.http import HttpResponse
from django.shortcuts import render
from .forms import AdministrationInformationForm


# Create your views here.
def location_create_view(request):
    form = AdministrationInformationForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form':form
    }
    return render(request, 'administration/create.html', context)
 
def location_detail_view(request):
    obj = AdministrationInformation.objects.get(id=2)
    context = {
        'object':obj
    }
    return render(request, 'administration/detail.html', context)