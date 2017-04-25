from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.Charfield(max_lengh=50)
    apellidos = models.Charfield(max_lengh=70)
    edad = models.IntegerField()
    telefono = models.Charfield(max_lengh=12)
    email = models.EmailField()
    domicilio = models.TextField()