from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import AdministrationInformation
from .forms import AdministrationInformationForm


# Create your views here.
def location_list_view(request):
    queryset = AdministrationInformation.objects.all()
    context ={
        'object_list': queryset
    }
    return render(request, 'administration/location_list.html', context)

def location_delete_view(request,id):
    obj = get_object_or_404(AdministrationInformation, id=id)
    if request.method =='POST':
        obj.delete()
        #make the redirect to another page
        return redirect('../../')
    
    context = {
        'object':obj
    }
    return render(request, 'administration/location_delete.html', context)
def location_create_view(request):
    form = AdministrationInformationForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AdministrationInformationForm()
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