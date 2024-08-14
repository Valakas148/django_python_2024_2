from django.db import models

from core.models import BaseModel


class AutoPark(BaseModel):
    class Meta:
        db_table = 'auto_parks'
        ordering = ['id']

    name = models.CharField(max_length=20)