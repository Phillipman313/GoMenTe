from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Persona(models.Model):
    opcionesSexo = (('H', 'Hombre'), ('M', 'Mujer'))

    #nombre = models.CharField('Nombre', max_length=50)
    #apellido1 = models.CharField('Primer apellido', max_length=50)
    apellido2 = models.CharField('Segudo apellido', max_length=50, null=True, blank=True)
    sexo = models.CharField('Sexo', max_length=5, choices=opcionesSexo)
    fechaNacimiento = models.DateField('Fecha nacimiento')
    celular = models.DecimalField('Celular', max_digits=30, decimal_places=0, null=True, blank=True)
    telefono = models.DecimalField('Telefono', max_digits=30, decimal_places=0)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    #correo = models.EmailField('Correo', unique=True)
    #usuario = models.CharField('Usuario', max_length=50)
    #clave = models.CharField('Clave', max_length=50)
    #confirmacion = models.CharField('Confirmar clave', max_length=50)