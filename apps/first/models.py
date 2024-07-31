from datetime import datetime

from django.core import validators as V
from django.db import models

from core.models import BaseModel

from apps.autoparks.models import AutoPark
from apps.first.choices.body_type_choices import BodyTypeChoices


# Create your models here.
class CarModel(BaseModel):
    class Meta:
        db_table = 'carmodel'
        ordering = ('-id',)

    brand = models.CharField(max_length=100, validators=(V.MinLengthValidator(2),))
    model = models.CharField(max_length=255)
    price = models.IntegerField(validators=(V.MinValueValidator(0), V.MaxValueValidator(1000000)))
    year = models.IntegerField(validators=(V.MaxValueValidator(datetime.now().year),))
    body_type = models.CharField(max_length=10, choices=BodyTypeChoices.choices)
    auto_park = models.ForeignKey(AutoPark, on_delete=models.CASCADE, related_name='cars')