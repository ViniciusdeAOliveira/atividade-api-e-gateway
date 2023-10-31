import uuid
from django.db import models

# MODEL - Service Order
class ServiceOrder(models.Model):
  id_os = models.AutoField(primary_key=True)
  number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
  description = models.TextField(max_length=255)
  
  def __str__(self):
    return "Service Order - " + str(self.number)
  
# MODEL - Equipment
class Equipment(models.Model):
  id_equipment = models.AutoField(primary_key=True)
  number = models.ForeignKey(
    ServiceOrder,
    to_field="number",
    on_delete=models.DO_NOTHING
  )
  index = models.IntegerField()
  description = models.CharField(max_length=150)
  failure = models.TextField(max_length=255)
  
  def __str__(self):
    return "Equipment - " + str(self.id_equipment)
