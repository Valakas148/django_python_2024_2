from django.db import models


class BodyTypeChoices(models.TextChoices):
    Universal = "Universal",
    HatchBack = "HatchBack",
    SUV = "SUV",
    Wagon = "Wagon",
    Coupe = "Coupe",
    Sedan = "Sedan"