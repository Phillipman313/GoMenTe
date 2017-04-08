from datetime import date

from django.shortcuts import render

# Create your views here.
from home.models import TipoIntegrante, Equipo

def equipoPorIntegrante():
    tipos = TipoIntegrante.objects.all()
    integrantes = Equipo.objects.all()
    equipo = {}
    for tipo in tipos:
        equipo[tipo.nombre] = integrantes.filter(idTipoIntegranteRef_id=tipo.pk)

def index(request):
    context = {'Y': date.today().year, 'datos': equipoPorIntegrante()}
    return render(request, 'home/index.html', context)
