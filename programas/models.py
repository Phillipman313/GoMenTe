from datetime import date

from django.db import models

# Create your models here.
from personas.models import Persona


class Programa(models.Model):
    nombre = models.CharField('Nombre', max_length=50, unique=True)
    descripcion = models.TextField('Descripcion')
    mentores = models.ManyToManyField(Persona, db_table='Mentores')

class Periodo(models.Model):
    nombre = models.CharField('Nombre', max_length=100, unique=True, editable=False)
    fechaInicio = models.DateField('Fecha de inicio', default=date.today())
    fechaFin = models.DateField('Fecha de fin', default=date.today())
    lugar = models.CharField('Nombre del lugar', max_length=100)
    direccion = models.TextField('Direccion', null=True, blank=True)
    idProgramaRef = models.ForeignKey(Programa, on_delete=models.PROTECT, verbose_name='Programa')

#class Mentores(models.Model):
#    idPersonaRef = models.ForeignKey(Persona, on_delete=models.PROTECT, verbose_name='Persona')
#    idProgramaRef = models.ForeignKey(Programa, on_delete=models.PROTECT)
