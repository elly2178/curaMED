from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import AdministrationInformation
from .forms import AdministrationInformationForm
from django.views.generic import (     
    UpdateView )

# Create your views here.
 
def location_view(request):
    queryset = AdministrationInformation.objects.all()
    context = {
        'object_list':queryset
    }
    return render(request, 'administration/location_list.html', context)

 
def location_delete_view(request,id):
    obj = get_object_or_404(AdministrationInformation, id=id)
    if request.method =='POST':
        obj.delete()
        return redirect('administration')
    
    context = {
        'object':obj
    }
    return render(request, 'administration/location_delete.html', context)

def location_create_view(request):
    form = AdministrationInformationForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AdministrationInformationForm()
        return redirect('administration')
    context = {
        'form':form
    }
    return render(request, 'administration/create.html', context)
 
def location_detail_view(request, id):
    obj = get_object_or_404(AdministrationInformation, id=id)
    form = AdministrationInformationForm(request.POST or None, instance=obj)
    print("REQUEST is " + str(dir(request)))
    if form.is_valid():
        print("FORM is valid")
        form.save()
        form = AdministrationInformationForm()
        return redirect('administration')
    context = {
        'object': obj
    }
    return render(request, 'administration/detail.html', context)

 
