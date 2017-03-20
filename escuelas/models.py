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
    administrativos = models.ManyToManyField(Persona, through='Administrativos', through_fields=('idEscuelaRef', 'idPersonaRef'), related_name='administrativos')
    estudiantes = models.ManyToManyField(Persona, through='Estudiantes', through_fields=('idEscuelaRef', 'idPersonaRef'), related_name='estudiantes')

class Puesto(models.Model):
    nombre = models.CharField('Nombre', max_length=50, unique=True)

class Administrativos(models.Model):
    idPersonaRef = models.ForeignKey(Persona, on_delete=models.PROTECT, verbose_name='Persona', related_name='personasA')
    idEscuelaRef = models.ForeignKey(Escuela, on_delete=models.PROTECT, verbose_name='Escuela', related_name='escuelasA')
    idPuestoRef = models.ForeignKey(Puesto, on_delete=models.PROTECT, verbose_name='Puesto', related_name='puestos')
    telefono = models.CharField('Telefono', max_length=30)
    correo = models.EmailField('Correo')

class Estudiantes(models.Model):
    idPersonaRef = models.ForeignKey(Persona, on_delete=models.PROTECT, verbose_name='Persona', related_name='personasE')
    idEscuelaRef = models.ForeignKey(Escuela, on_delete=models.PROTECT, verbose_name='Escuela', related_name='escuelasE')
    fechaInicio = models.DateField('Admision')
    fechaFin = models.DateField('Salida', null=True, blank=True)