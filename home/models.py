from django.db import models

# Create your models here.
from django.utils import timezone
from redactor.fields import RedactorField

from personas.models import Persona


class TipoIntegrante(models.Model):
    nombre = models.CharField('Nombre', max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Integrante(models.Model):
    descripcion = models.TextField('Descripcion')
    idPersonaRef = models.ForeignKey(Persona, on_delete=models.PROTECT, verbose_name='Persona')
    idTipoIntegranteRef = models.ForeignKey(TipoIntegrante, on_delete=models.PROTECT, verbose_name='Tipo integrante')

class Tercero(models.Model):
    nombre = models.CharField('Nombre', max_length=100, unique=True)
    url = models.URLField('Direccion web')
    logo = models.ImageField('Logo', upload_to='logos/terceros/')

    def __str__(self):
        return self.nombre

class Acerca(models.Model):
    informacion = RedactorField(verbose_name='Informacion')
    actualizacion = models.DateTimeField('Ultima actualizacion', default=timezone.now())

    class Meta:
        verbose_name = 'Acerca'
        verbose_name_plural = 'Acerca'