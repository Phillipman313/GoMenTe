from django.db import models

# Create your models here.
from personas.models import Persona
from sesiones.models import Sesion, Grupo


class Participantes(models.Model):
    idPersonaRef = models.ForeignKey(Persona, on_delete=models.PROTECT, verbose_name='Persona', related_name='personasI')
    idGrupoRef = models.ForeignKey(Grupo, on_delete=models.PROTECT, verbose_name='Grupo', related_name='gruposI')

class Competencia(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    descripcion = models.TextField('Descripcion', null=True, blank=True)
    idSesionRef = models.ForeignKey(Sesion, on_delete=models.PROTECT, verbose_name='Sesion')
    participantesCompetencias = models.ManyToManyField(Participantes, through='ParticipantesCompetencias', through_fields=('idCompetenciaRef', 'idPersonaRef'))

class ParticipantesCompetencias(models.Model):
    porcentaje = models.FloatField('Porcentaje')
    descripcion = models.TextField('Descripcion', null=True, blank=True)
    idPersonaRef = models.ForeignKey(Persona, on_delete=models.PROTECT, verbose_name='Persona')
    idGrupoRef = models.ForeignKey(Grupo, on_delete=models.PROTECT, verbose_name='Grupo')
    idCompetenciaRef = models.ForeignKey(Competencia, on_delete=models.PROTECT, verbose_name='Competencia')

    class Meta:
        unique_together = ('idPersonaRef', 'idGrupoRef', 'idCompentenciaRef')
        verbose_name = 'Participante'
        verbose_name_plural = 'Participantes'