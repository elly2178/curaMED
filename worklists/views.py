from django.shortcuts import render
from .models import WorklistInformation
from .forms import WorklistInformationForm
from django.views import View
from django.shortcuts import (
    render, get_object_or_404, redirect)
# Create your views here.
class WorklistCreateView(View):
    #works
    template_name = 'worklists/worklist_create.html'
    def get(self, request, *args, **kwargs):
        # get method
        form = WorklistInformationForm()
        print('this is the get')
        context = {
            'form':form
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


def worklist_list_view(request):
    queryset = WorklistInformation.objects.all()
    context ={
        'object_list': queryset
    }
    return render(request, 'worklists/worklist_list.html', context)