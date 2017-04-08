from django.db import models

# Create your models here.
from personas.models import Persona


class TipoIntegrante(models.Model):
    nombre = models.CharField('Nombre', max_length=50)

class Equipo(models.Model):
    descripcion = models.TextField('Descripcion')
    idPersonaRef = models.ForeignKey(Persona, on_delete=models.PROTECT, verbose_name='Persona')
    idTipoIntegranteRef = models.ForeignKey(TipoIntegrante, on_delete=models.PROTECT, verbose_name='Tipo integrante')