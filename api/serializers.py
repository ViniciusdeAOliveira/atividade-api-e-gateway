from rest_framework import serializers
from .models import *

# SERIALIZADOR - Service Order
class ServiceOrderSerializer(serializers.ModelSerializer):
  class Meta:
    model = ServiceOrder
    fields = "__all__"
    
# SERIALIZADOR - Equipment
class Equipmentserializer(serializers.ModelSerializer):
  class Meta:
    model = Equipment
    fields = "__all__"