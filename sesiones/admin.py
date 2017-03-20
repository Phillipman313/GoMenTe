from django.contrib import admin

# Register your models here.
from sesiones.models import Sesion, Grupo, TipoParticipante, Participantes

admin.site.register(Sesion)
admin.site.register(Grupo)
admin.site.register(TipoParticipante)
admin.site.register(Participantes)