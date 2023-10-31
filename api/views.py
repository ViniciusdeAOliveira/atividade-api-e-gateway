from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework import permissions
from django_filters.rest_framework import *

# VIEW - Service Order - GET E POST
class ServiceOrderViewGetPost(generics.ListCreateAPIView):
  queryset = ServiceOrder.objects.all()
  serializer_class = ServiceOrderSerializer
  filterset_fields = ['id_os', 'number', 'description'] 
  
# VIEW - Service Order - GET BY NUMBER
class ServiceOrderViewGetBynumber(generics.ListAPIView):
  queryset = ServiceOrder.objects.all()
  serializer_class = ServiceOrderSerializer
  lookup_field = 'number'
  filterset_fields = ['id_os', 'number', 'description']
  
  # RETURN THE SERVICE ORDER WITH THE NUMBER SEARCHED
  def get_queryset(self):
    number = self.kwargs['number']
    return ServiceOrder.objects.filter(number=number)

# VIEW - EQUIPMENT - GET BY NÚMERO OF SERVICE ORDER
class EquipmentBynumberOs(generics.ListCreateAPIView):
  serializer_class = Equipmentserializer
  lookup_field = 'number'
  filterset_fields = ['id_equipment', 'index', 'description', 'failure', 'number'] 
  
  def get_queryset(self):
    number = self.kwargs['number']
    return Equipment.objects.filter(number__number=number)
  
# VIEW - EQUIPAMENTO - GET BY NUMBER OF SERVICE ORDER AND INDEX
class EquipmentBynumberOsindex(generics.ListAPIView):
  serializer_class = Equipmentserializer
  filterset_fields = ['id_equipment', 'index', 'description', 'failure', 'number'] 
  
  def get_queryset(self):
    number = self.kwargs['number']
    index = self.kwargs['index']
    
    return Equipment.objects.filter(number__number=number, index=index)
    
  
# VIEW - EQUIPAMENTO GET BY DESCRIPTION
class EquipmentBydescription(generics.ListAPIView):
  serializer_class = Equipmentserializer
  lookup_field = 'description'
  filterset_fields = ['id_equipment', 'index', 'description', 'failure', 'number'] 
  
  def get_queryset(self):
    description = self.kwargs['description']
    return Equipment.objects.filter(description=description)
  