from django.urls import path
from .views import(
    patient_create_view, 
    patient_delete_view, 
    patient_list_view, 
    patient_search_view
     #, patient_edit_view
)

urlpatterns = [
    path('patients/create', patient_create_view, name ='patientCreate'),
    path('patients/list/<int:id>/delete/', patient_delete_view, name ='patientDelete'),
    path('patients/list/', patient_list_view, name ='patients'),
    # path('patients/list/<int:id>/edit/', patient_edit_view, name ='patientEdit'),
    path('patients/search', patient_search_view, name = 'patientSearch'),
]
