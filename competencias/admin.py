from django.contrib import admin

# Register your models here.
from competencias.models import Competencia, ParticipantesCompetencias

admin.site.register(Competencia)
admin.site.register(ParticipantesCompetencias)