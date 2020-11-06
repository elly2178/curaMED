from django.urls import path
from .views import(
     location_create_view, 
     location_detail_view, 
     location_delete_view, 
     location_list_view
)

urlpatterns = [
    #path('administration/', homepage_administration_view, name ='administration'),
    path('administration/create', location_create_view, name ='locationCreate'),
    path('administration/<int:id>/delete/', location_delete_view, name ='locationDelete'),
    path('administration/list', location_list_view, name ='administration'),
]
