from django.contrib import admin

# Register your models here.
from tabbed_admin.admin import TabbedModelAdmin

from escuelas.models import TipoEscuela, Escuela, Puesto, Administrativos, Estudiantes

admin.site.register(TipoEscuela)
admin.site.register(Puesto)

class EstudiantesInline(admin.StackedInline):
    model = Estudiantes

class AdministrativosInline(admin.StackedInline):
    model = Administrativos

class EscuelaAdmin(TabbedModelAdmin):
    model = Escuela

    tab_escuela = ((None, {'fields': ('nombre', 'descripcion', 'idTipoEscuelaRef', 'idDistritoRef')}), )
    tab_estudiantes = (EstudiantesInline, )
    tab_administrativos = (AdministrativosInline, )

    tabs = [('Escuela', tab_escuela), ('Estudiantes', tab_estudiantes), ('Administrativos', tab_administrativos)]

admin.site.register(Escuela, EscuelaAdmin)


