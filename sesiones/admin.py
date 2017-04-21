from django.contrib import admin

# Register your models here.
from tabbed_admin.admin import TabbedModelAdmin

from sesiones.models import Sesion, Grupo, Facilitadores, TipoFacilitador

admin.site.register(Sesion)
admin.site.register(TipoFacilitador)

class FacilitadoresInline(admin.StackedInline):
    model = Facilitadores

class ParticipantesInline(admin.StackedInline):
    model = Grupo.participantes.through

class GrupoAdmin(TabbedModelAdmin):
    model = Grupo

    tab_grupo = ((None, {'fields': ('idProgramaRef', 'nombre')}), FacilitadoresInline)
    tab_participantes = (ParticipantesInline, )

    tabs = [('Grupo', tab_grupo), ('Participantes', tab_participantes)]

admin.site.register(Grupo, GrupoAdmin)