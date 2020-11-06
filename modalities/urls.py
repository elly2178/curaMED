from django.urls import path
from .views import(
    modality_create_view, 
    modality_detail_view, 
    modality_delete_view, 
    modality_list_view
)
#own imports
from django.views.generic import RedirectView
from pages.views import homepage_view, homepage_administration_view, homepage_modalities_view

from administration.views import location_create_view, location_detail_view, location_delete_view, location_list_view
 
urlpatterns = [
    #path('modalities/', homepage_modalities_view, name ='modalities'),
    path('modalities/create', modality_create_view, name ='modalityCreate'),
    path('modalities/<int:id>/delete/', modality_delete_view, name ='modalityDelete'),
    path('modalities/list', modality_list_view, name ='modalities'),

    #path('administration/', homepage_administration_view, name ='administration'),
    path('administration/create', location_create_view, name ='locationCreate'),
    path('administration/<int:id>/delete/', location_delete_view, name ='locationDelete'),
    path('administration/list', location_list_view, name ='administration'),
]
