from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Mascota(models.model):
    folio = models.CharField(max_lengh=10, primary_key=True)
    nombre = models.CharField(max_lengh=50)
    sexo = models.CharField(max_lengh=10)
    edad_aproximada = models.IntegerField()
    fecha_rescate = models.DateField()

        