from django.db import models
import uuid


class TimestampedModel(models.Model):
    class Meta:
       abstract = True
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UUIDModel(models.Model):
    class Meta:
        abstract = True
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
class BaseModel(TimestampedModel, UUIDModel):
    pass