from datetime import date

from django.db import models

# Create your models here.
from lugares.models import Distrito
from personas.models import Persona
from programas.models import Periodo


class Sesion(models.Model):
    nombre = models.CharField('Nombre', max_length=100, unique=True)
    fecha = models.DateField('Fecha', default=date.today)
    inicio = models.TimeField('Hora de inicio', default=date.today)
    fin = models.TimeField('Hora de fin', default=date.today)
    lugar = models.CharField('Nombre del lugar', max_length=100)
    direccion = models.TextField('Direccion', null=True, blank=True)
    latitud = models.DecimalField('Latitud', max_digits=30, decimal_places=10, null=True, blank=True, editable=False)
    longitud = models.DecimalField('Longitud', max_digits=30, decimal_places=10, null=True, blank=True, editable=False)
    idPeriodoRef = models.ForeignKey(Periodo, on_delete=models.PROTECT, verbose_name='Periodo')
    idDistritoRef = models.ForeignKey(Distrito, on_delete=models.PROTECT, verbose_name='Distrito')

class Grupo(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    idSesionRef = models.ForeignKey(Sesion, on_delete=models.PROTECT, verbose_name='Grupo')
    participantes = models.ManyToManyField(Persona, through='Participantes', through_fields=('idGrupoRef', 'idPersonaRef'), related_name='participantes')
    facilitadores = models.ManyToManyField(Persona, related_name='facilitadores')

class TipoParticipante(models.Model):
    nombre = models.CharField('Nombre', max_length=50, unique=True)

class Participantes(models.Model):
    idPersonaRef = models.ForeignKey(Persona, on_delete=models.PROTECT, verbose_name='Persona', related_name='personasI')
    idGrupoRef = models.ForeignKey(Grupo, on_delete=models.PROTECT, verbose_name='Grupo', related_name='gruposI')
    idTipoParticipanteRef = models.ForeignKey(TipoParticipante, on_delete=models.PROTECT, verbose_name='Tipo de participante')