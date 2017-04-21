from datetime import date

from django.db import models

# Create your models here.
from personas.models import Persona
from programas.models import Programa


class Sesion(models.Model):
    nombre = models.CharField('Nombre', max_length=100, unique=True)
    fecha = models.DateField('Fecha', default=date.today)
    inicio = models.TimeField('Hora de inicio', default=date.today)
    fin = models.TimeField('Hora de fin', default=date.today)
    idPrograma = models.ForeignKey(Programa, on_delete=models.PROTECT, verbose_name='Programa')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Sesion'
        verbose_name_plural = 'Sesiones'

class Grupo(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    idProgramaRef = models.ForeignKey(Programa, on_delete=models.PROTECT, verbose_name='Programa')
    facilitadores = models.ManyToManyField(Persona, through='Facilitadores', through_fields=('idGrupoRef', 'idPersonaRef'), related_name='facilitadores')
    participantes = models.ManyToManyField(Persona, related_name='participantes', db_table='Participantes')

    def __str__(self):
        return self.nombre

class TipoFacilitador(models.Model):
    nombre = models.CharField('Nombre', max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Facilitadores(models.Model):
    idPersonaRef = models.ForeignKey(Persona, on_delete=models.PROTECT, verbose_name='Persona', related_name='personas_facilitadores')
    idGrupoRef = models.ForeignKey(Grupo, on_delete=models.PROTECT, verbose_name='Grupo', related_name='grupos_facilitadores')
    idTipoFacilitadorRef = models.ForeignKey(TipoFacilitador, on_delete=models.PROTECT, verbose_name='Tipo de facilitador')