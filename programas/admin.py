from django.contrib import admin

# Register your models here.
from programas.models import Programa, Periodo

admin.site.register(Programa)
admin.site.register(Periodo)