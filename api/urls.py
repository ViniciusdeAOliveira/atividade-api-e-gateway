from django.urls import path
from . import views

# URLS
urlpatterns = [
  # URL - CREATE AND/OR GET ALL SERVICE ORDERS
   
  path(
    'v1/os/',
    views.ServiceOrderViewGetPost.as_view(),
    name='os-get-all'
  ),
  
  # URL - GET THE SERVICE ORDER BY NUMBER
  path(
    'v1/os/<str:number>/',
    views.ServiceOrderViewGetBynumber.as_view(),
    name='os-get-by-number'
  ),
  
  # URL - GET ALL EQUIPMENTS OF A SERVICE ORDER

  path(
    'v1/os/<str:number>/Equipment/',
    views.EquipmentBynumberOs.as_view(),
    name='Equipment-get-by-number-os'
  ),
  
  # URL - GET ALL EQUIPMENTS OF A SERVICE ORDER AND WITH A INDEX

  path(
    'v1/os/<str:number>/Equipment/<int:index>/',
    views.EquipmentBynumberOsindex.as_view(),
    name='Equipment-get-by-number-os-index'
  ),
  
  # URL - GET ALL EQUIPMENTS WITH AN ESPECIFIC DESCRIPTION
  
  path(
    'v1/os/Equipment/<str:description>/',
    views.EquipmentBydescription.as_view(),
    name='Equipment-obter-por-description'
  ),
]
