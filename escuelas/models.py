from datetime import date

from django.db import models

# Create your models here.
from lugares.models import Distrito
from personas.models import Persona


class TipoEscuela(models.Model):
    nombre = models.CharField('Nombre', max_length=50, unique=True)

class Escuela(models.Model):
    nombre = models.CharField('Nombre', max_length=50, unique=True)
    descripcion = models.TextField('Descripcion', null=True, blank=True)
    idTipoEscuelaRef = models.ForeignKey(TipoEscuela, on_delete=models.PROTECT, verbose_name='Tipo de escuela')
    idDistritoRef = models.ForeignKey(Distrito, on_delete=models.PROTECT, verbose_name='Distrito')
    administrativos = models.ManyToManyField(Persona, through='Administrativos', through_fields=('idPersonaRef', 'idEscuelaRef'), db_table='Administrativos')
    estudiantes = models.ManyToManyField(Persona, through='Estudiantes', through_fields=('idPersonaRef', 'idEscuelaRef'), db_table='Estudiantes')

class Puesto(models.Model):
    nombre = models.CharField('Nombre', max_length=50, unique=True)

class Administrativos(models.Model):
    telefono = models.DecimalField('Telefono', max_digits=50, decimal_places=0)
    correo = models.EmailField('Correo')
    idPersonaRef = models.ForeignKey(Persona, on_delete=models.PROTECT, verbose_name='Persona')
    idEscuelaRef = models.ForeignKey(Escuela, on_delete=models.PROTECT, verbose_name='Escuela')
    idPuestoRef = models.ForeignKey(Puesto, on_delete=models.PROTECT, verbose_name='Puesto')

class Estudiantes(models.Model):
    fechaInicio = models.DateField('Admision', default=date.today())
    fechaFin = models.DateField('Salida', null=True, blank=True)
    idPersonaRef = models.ForeignKey(Persona, on_delete=models.PROTECT, verbose_name='Persona')
    idEscuelaRef = models.ForeignKey(Escuela, on_delete=models.PROTECT, verbose_name='Escuela')