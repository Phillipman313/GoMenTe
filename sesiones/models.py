from datetime import date

from django.db import models

# Create your models here.
from personas.models import Persona
from programas.models import Periodo


class Sesion(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    fecha = models.DateField('Fecha', default=date.today())
    inicio = models.TimeField('Hora de inicio', default=date.today())
    fin = models.TimeField('Hora de fin', default=date.today())
    idPeriodoRef = models.ForeignKey(Periodo, on_delete=models.PROTECT)

class Grupo(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    idSesionRef = models.ForeignKey(Sesion, on_delete=models.PROTECT)
    participantes = models.ManyToManyField(Persona, through='Participantes', through_fields=('idPersonaRef', 'idGrupoRef'), db_table='Participantes')

class TipoParticipante(models.Model):
    nombre = models.CharField('Nombre', max_length=50, unique=True)

class Participantes(models.Model):
    idPersonaRef = models.ForeignKey(Persona, on_delete=models.PROTECT, verbose_name='Persona')
    idGrupoRef = models.ForeignKey(Grupo, on_delete=models.PROTECT, verbose_name='Grupo')
    idTipoParticipanteRef = models.ForeignKey(TipoParticipante, on_delete=models.PROTECT, verbose_name='Tipo de participante')