from django.db import models

# Create your models here.
from personas.models import Persona


class Equipo(models.Model):
    descripcion = models.TextField('Descripcion')
    idPersonaRef = models.ForeignKey(Persona, on_delete=models.PROTECT, verbose_name='Persona')