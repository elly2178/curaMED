from django.shortcuts import render
from .models import WorklistInformation
from patients.models import PatientInformation
from .forms import WorklistInformationForm
from django.views import View
from django.shortcuts import (
    render, get_object_or_404, redirect)
import datetime
# Create your views here.
class WorklistCreateView(View):
    #works
    template_name = 'worklists/worklist_create.html'
    def get(self, request, *args, **kwargs):
        patient_id = request.GET.get('patient-id')
        patient = get_object_or_404(PatientInformation, id=patient_id)
        # get method
        form = WorklistInformationForm(request.POST)
        print('this is the get')
        current_date = datetime.datetime.today()
        
        print(current_date)
        context = {
             
            'date':current_date,
            'patient': patient,
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        #post method 
        
        form = WorklistInformationForm(request.POST)
        print('somethign wong'+ str(form))
        if form.is_valid():
            print('you are in the if')
            form.save()
            return redirect('patients')
            print('worklist erstellt')
        context = { 'form':form }
        return render(request, self.template_name, context)
  
# worklists are not saved...
def worklist_list_view(request):
    queryset = WorklistInformation.objects.all()
    context ={
        'object_list': queryset
    }
    return render(request, 'worklists/worklist_list.html', context)