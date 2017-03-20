from datetime import date

from django.db import models

# Create your models here.
from personas.models import Persona

#mentores no tiene through_fields porque es una tabla intermedia sin campos adicionales
class Programa(models.Model):
    nombre = models.CharField('Nombre', max_length=50, unique=True)
    descripcion = models.TextField('Descripcion')
    mentores = models.ManyToManyField(Persona, db_table='Mentores')

class Periodo(models.Model):
    nombre = models.CharField('Nombre', max_length=100, unique=True, editable=False)
    fechaInicio = models.DateField('Fecha de inicio', default=date.today)
    fechaFin = models.DateField('Fecha de fin', default=date.today)
    idProgramaRef = models.ForeignKey(Programa, on_delete=models.PROTECT, verbose_name='Programa')

#class Mentores(models.Model):
#    idPersonaRef = models.ForeignKey(Persona, on_delete=models.PROTECT, verbose_name='Persona')
#    idProgramaRef = models.ForeignKey(Programa, on_delete=models.PROTECT)
