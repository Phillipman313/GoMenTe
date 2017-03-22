from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver


class Persona(models.Model):
    opcionesSexo = (('H', 'Hombre'), ('M', 'Mujer'))

    nombre = models.CharField('Nombre', max_length=50)
    apellido1 = models.CharField('Primer apellido', max_length=50)
    apellido2 = models.CharField('Segudo apellido', max_length=50, null=True, blank=True)
    sexo = models.CharField('Sexo', max_length=5, choices=opcionesSexo)
    identificacion = models.CharField('Identificacion', max_length=50, unique=True)
    fecha = models.DateField('Fecha nacimiento')
    celular = models.CharField('Celular', max_length=30, null=True, blank=True)
    telefono = models.CharField('Telefono', max_length=30, null=True, blank=True)
    correo = models.EmailField('Correo', unique=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    #usuario = models.CharField('Usuario', max_length=50)
    #clave = models.CharField('Clave', max_length=50)
    #confirmacion = models.CharField('Confirmar clave', max_length=50)

@receiver(post_save, sender=User)
def crearPersona(sender, **kwargs):
    if kwargs.get('created', False):
        Persona.objects.get_or_create(usuario=kwargs.get('instance'))

