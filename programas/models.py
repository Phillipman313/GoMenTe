from datetime import date

from django.db import models

# Create your models here.
from photologue.models import Gallery

from home.models import Tercero
from lugares.models import Distrito
from personas.models import Persona

#mentores no tiene through_fields porque es una tabla intermedia sin campos adicionales
class Programa(models.Model):
    nombre = models.CharField('Nombre', max_length=50, unique=True)
    corto = models.CharField('Corto', max_length=50, unique=True)
    descripcion = models.TextField('Descripcion')
    fechaInicio = models.DateField('Fecha de inicio', default=date.today)
    fechaFin = models.DateField('Fecha de fin', default=date.today)
    lugar = models.CharField('Nombre del lugar', max_length=100)
    direccion = models.TextField('Direccion', null=True, blank=True)
    latitud = models.DecimalField('Latitud', max_digits=30, decimal_places=10, null=True, blank=True, editable=False)
    longitud = models.DecimalField('Longitud', max_digits=30, decimal_places=10, null=True, blank=True, editable=False)
    logo = models.ImageField('Logo', upload_to='logos/programas/')
    galeria = models.OneToOneField(Gallery, verbose_name='Galeria')
    mentores = models.ManyToManyField(Persona, related_name='mentores', db_table='Mentores')
    capacitadores = models.ManyToManyField(Persona, related_name='capacitadores', db_table='Capacitadores')
    patrocinadores = models.ManyToManyField(Tercero, related_name='patrocinadores', db_table='Patrocinadores')
    idDistritoRef = models.ForeignKey(Distrito, on_delete=models.PROTECT, verbose_name='Distrito')

    def __str__(self):
        return self.nombre

#class Periodo(models.Model):
#    nombre = models.CharField('Nombre', max_length=100, unique=True, editable=False)
#    fechaInicio = models.DateField('Fecha de inicio', default=date.today)
#    fechaFin = models.DateField('Fecha de fin', default=date.today)
#    idProgramaRef = models.ForeignKey(Programa, on_delete=models.PROTECT, verbose_name='Programa')

#    def __str__(self):
#        return self.nombre

#class Mentores(models.Model):
#    idPersonaRef = models.ForeignKey(Persona, on_delete=models.PROTECT, verbose_name='Persona')
#    idProgramaRef = models.ForeignKey(Programa, on_delete=models.PROTECT)
