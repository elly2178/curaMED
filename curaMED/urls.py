"""curaMED URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 

#own imports
from django.views.generic import RedirectView
from pages.views import homepage_view

from patients.views import(
    
    patient_delete_view, 
    patient_list_view, 
    patient_search_view,
    patient_search_result_view,
    patient_detail_view,
    PatientCreateView,
    patient_delete_view
     
)
from modalities.views import(
    modality_create_view, 
    modality_detail_view, 
    modality_delete_view, 
    modality_list_view
)
from administration.views import(
     location_create_view, 
     location_detail_view, 
     location_delete_view, 
     location_view 
)

from worklists.views import (
    WorklistCreateView,
    worklist_list_view
)
urlpatterns = [
    path(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
    path('admin/', admin.site.urls),
    path('', homepage_view, name = 'home'),
 
    path('patients/list/create/', PatientCreateView.as_view(), name ='patientCreate'),
    path('patients/list/<int:id>/delete/', patient_delete_view, name ='patientDelete'),
   
    path('patients/list/', patient_list_view, name ='patients'),
    path('patients/search/', patient_search_view, name = 'patientSearch'),
    path('patients/search/result/', patient_search_result_view, name = 'searchResult'),
    path('patients/<int:id>/detail/', patient_detail_view, name ='patientDetail'),
    path('patients/<int:id>/delete/', patient_delete_view, name ='patientDelete'),

    path('modalities/create/', modality_create_view, name ='modalityCreate'),
    path('modalities/<int:id>/delete/', modality_delete_view, name ='modalityDelete'),
    path('modalities/<int:id>/detail/', modality_detail_view, name ='modalityDetail'),
    path('modalities/list/', modality_list_view, name ='modalities'),

    path('administration/create/', location_create_view, name ='locationCreate'),
    path('administration/<int:id>/delete/', location_delete_view, name ='locationDelete'),
    path('administration/list/', location_view, name ='administration'),
    path('administration/list/<int:id>/detail/', location_detail_view, name ='locationDetail'),
   
    path('worklists/create/', WorklistCreateView.as_view(), name ='worklistCreate'),
    path('worklists/list/', worklist_list_view, name ='worklistList'),
]
