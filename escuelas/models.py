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

    def __str__(self):
        return self.nombre

class Puesto(models.Model):
    nombre = models.CharField('Nombre', max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Administrativos(models.Model):
    idPersonaRef = models.ForeignKey(Persona, on_delete=models.PROTECT, verbose_name='Persona', related_name='personas_administrativos')
    idEscuelaRef = models.ForeignKey(Escuela, on_delete=models.PROTECT, verbose_name='Escuela', related_name='escuelas_administrativos')
    idPuestoRef = models.ForeignKey(Puesto, on_delete=models.PROTECT, verbose_name='Puesto', related_name='puestos')
    telefono = models.CharField('Telefono', max_length=30)
    correo = models.EmailField('Correo')

    class Meta:
        verbose_name = 'Administrativo'
        verbose_name_plural = 'Administrativos'

class Estudiantes(models.Model):
    idPersonaRef = models.ForeignKey(Persona, on_delete=models.PROTECT, verbose_name='Persona', related_name='personas_estudiantes')
    idEscuelaRef = models.ForeignKey(Escuela, on_delete=models.PROTECT, verbose_name='Escuela', related_name='escuelas_estudiantes')
    fechaInicio = models.DateField('Admision')
    fechaFin = models.DateField('Salida', null=True, blank=True)

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'