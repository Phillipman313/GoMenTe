from django.db import models

# Create your models here.


class Provincia(models.Model):
    nombre = models.CharField('Nombre', max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Canton(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    idProvinciaRef = models.ForeignKey(Provincia, on_delete=models.PROTECT, verbose_name='Provincia')

    def __str__(self):
        return self.nombre

class Distrito(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    idCantonRef = models.ForeignKey(Canton, on_delete=models.PROTECT, verbose_name='Canton')

    def __str__(self):
        return self.nombre