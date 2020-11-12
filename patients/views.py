
from django.shortcuts import (
    render, get_object_or_404, redirect)
from django.urls import reverse
from .models import PatientInformation
from .forms import PatientInformationForm
from django.db.models import Q


# import for detail, list view
from django.views.generic import DetailView
#from django.urls import reverse_lazy

#import for list view
from django.views import View
# Create your views here.
# asta e nou
# Class PatientUpdateView(View):
#     template_name = 'patient/patient_update.html'
def patient_update_view(request, id= id):
    obj = get_object_or_404(PatientInformation, id= id)
    form = PatientInformationForm(request.POST or None, instance =obj)
    if form.is_valid():
        form.save()
    context = {
        'form' : form
    }
    return render(request, 'patient/patient_create.html', context)

# asta e nou
# class PatientDetailView(DetailView):
#     template_name = 'patient/patient_detail.html'
#     def get(self, request, id = None, *args, **kwargs):
#         context = {}
#         if id is not None:
#            obj = get_object_or_404(PatientInformation, id =id)
#            context['object'] = obj
        
#         #return redirect('patients')
#         return render(request, self.template_name, context)

def patient_detail_view(request, id):
    obj = get_object_or_404(PatientInformation, id=id)
    form = PatientInformationForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        form = PatientInformationForm()
        return redirect('patients')
    context = {
        'object': obj
    }
    return render(request, 'patient/patient_detail.html', context)

# def patient_detail_view(request, id):
#     obj = get_object_or_404(PatientInformation, id=id)
#     context ={
#         'object' : obj
#     }
#     return render(request, 'patient/patient_detail.html', context)

# def patient_search_view(request):
#     if request.method =='GET':
#         search = request.GET.get('search')
#         post = PatientInformation.objects.all().filter(id=search)
#         context = {
#             'post': post
#         }
#         return render(request, 'patient/patient_list.html', context )

# def patient_search_view(queryset=None):
#     queryset = []
#     queriesList = query.split(" ")
#     for q in queriesList:
#         patients = PatientInformation.objects.filter(
#             Q(first_name_icontains=q)|
#             # | or
#             Q(second_name_icontains=q)
#         ).distinct()
#         for patient in patients:
#             queryset.append(patient)
#     # return unique set        
#     return list(set(queryset))

# def patient_search_result_view(request):
#     context = {

#     }
#     query = ''
#     if request.GET:
#         query = request.GET['g']
#         context['query'] = str(query)
#     return render(request, 'patients/patients_list.html', context)
 
def patient_list_view(request):
    queryset = PatientInformation.objects.all()
    context ={
        'object_list': queryset
    }
    return render(request, 'patient/patient_list.html', context)

   
def patient_delete_view(request,id):
    obj = get_object_or_404(PatientInformation, id=id)
    if request.method =='POST':
        obj.delete()
        #make the redirect to another page
        # for modalitäten --> redirect to mod anzeigen
        return redirect('patients')
    context = {
        'object':obj
    }
    return render(request,'patient/patient_delete.html', context)

#similar cu create wl
class PatientCreateView(View):
    #works
    template_name = 'patient/patient_create.html'
    def get(self, request, *args, **kwargs):
        # get method
        form = PatientInformationForm()
        context = {
            'form':form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        #post method 
        form = PatientInformationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patients')
        context = { 'form':form }
        return render(request, self.template_name, context)

# def patient_create_view(request):
    
#     form = PatientInformationForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = PatientInformationForm()
#     context = {
#         'form':form
#     }
#     return render(request, 'patient/patient_ create.html', context)

