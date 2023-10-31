from django.contrib import admin
from .models import ServiceOrder, Equipment

#ADMIN - Equipments
class EquipmentAdmin(admin.ModelAdmin):
  list_display = ("id_equipment", "number", "index", "description", "failure")


# ADMIN - Service Order
class ServiceOrderAdmin(admin.ModelAdmin):
  list_display = ("id_os", "number", "description")
  readonly_fields = ("number",)
  

  
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(ServiceOrder, ServiceOrderAdmin)
