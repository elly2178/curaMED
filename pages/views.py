from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage_view(request,*args, **kwargs):
    # returning a html document
    return render(request, 'home.html',{})


# def homepage_patients_view(request, *args, **kwargs):
    
#     return render(request, "patient/detail.html", {})

def homepage_modalities_view(request, *args, **kwargs):
    my_context ={
        'my_text':'this is a modality',
        'my_id': 123
    }
    return render(request, "modality/detail.html", my_context)

def homepage_administration_view(request, *args, **kwargs):
    return render(request, "administration/detail.html", {})
