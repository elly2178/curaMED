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
from pages.views import homepage_view, homepage_administration_view, homepage_modalities_view
from patients.views import patient_detail_view, patient_create_view
from modalities.views import modality_create_view, modality_detail_view
from administration.views import location_create_view, location_detail_view
# homepage_patients_view,
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage_view, name = 'home'),
    #path('patients/', homepage_patients_view, name ='patientInformation'),

    path('patient/', patient_detail_view, name ='patientDetail'),
    path('patient/create', patient_create_view, name ='patientCreate'),

    path('modalities/', homepage_modalities_view, name ='modality'),
    path('modalities/create', modality_create_view, name ='modalityCreate'),
    
    path('administration/', homepage_administration_view, name ='administration'),
    path('administration/create', location_create_view, name ='locationCreate'),
]
