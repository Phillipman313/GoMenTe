from django.contrib import admin

# Register your models here.
from tabbed_admin.admin import TabbedModelAdmin

from programas.models import Programa

class MentoresInline(admin.StackedInline):
    model = Programa.mentores.through

class CapacitadoresInline(admin.StackedInline):
    model = Programa.capacitadores.through

class PatrocinadoresInline(admin.StackedInline):
    model = Programa.patrocinadores.through
    verbose_name = 'Patrocinador'
    verbose_name_plural = 'Patrocinadores'

class ProgramaAdmin(TabbedModelAdmin):
    model = Programa

    tab_programa = ((None, {'fields': ('nombre', 'corto', 'descripcion', 'fechaInicio', 'fechaFin', 'lugar', 'direccion', 'idDistritoRef', 'logo', 'galeria')}), PatrocinadoresInline)
    tab_mentores = (MentoresInline, )
    tab_capacitadores = (CapacitadoresInline, )

    tabs = [('Programas', tab_programa), ('Mentores', tab_mentores), ('Capacitadores', tab_capacitadores)]

admin.site.register(Programa, ProgramaAdmin)