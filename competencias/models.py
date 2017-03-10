from django.db import models

# Create your models here.
from personas.models import Persona
from sesiones.models import Sesion, Participantes, Grupo


class Competencia(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    descripcion = models.TextField('Descripcion', null=True, blank=True)
    idSesionRef = models.ForeignKey(Sesion, on_delete=models.PROTECT, verbose_name='Sesion')
    participantesCompetencias = models.ManyToManyField(Participantes, through='ParticipantesCompetencias', through_fields=('idPersonaRef', 'idGrupoRef', 'idCompetenciaRef'), db_table='ParticipantesCompetencias')

class ParticipantesCompetencias(models.Model):
    idPersonaRef = models.ForeignKey(Persona, on_delete=models.PROTECT)
    idGrupoRef = models.ForeignKey(Grupo, on_delete=models.PROTECT)
    idCompetenciaRef = models.ForeignKey(Competencia, on_delete=models.PROTECT)
    porcentaje = models.FloatField('Porcentaje')
    descripcion = models.TextField('Descripcion')