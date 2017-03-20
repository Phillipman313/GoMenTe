from django.contrib import admin

# Register your models here.
from escuelas.models import TipoEscuela, Escuela, Puesto, Administrativos, Estudiantes

admin.site.register(TipoEscuela)
admin.site.register(Escuela)
admin.site.register(Puesto)
admin.site.register(Administrativos)
admin.site.register(Estudiantes)
