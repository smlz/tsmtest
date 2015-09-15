from django.db import models
from django_extensions.db.models import TimeStampedModel

# Create your models here.

class MyTimeStampedModel(TimeStampedModel):
    some_other_field = models.IntegerField()
