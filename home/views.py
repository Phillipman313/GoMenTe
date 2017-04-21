from datetime import date

from django.shortcuts import render

# Create your views here.
from home.models import TipoIntegrante, Integrante


#def acerca():
#    return Sobre.objects.all().first()

def equipoPorIntegrante():
    tipos = TipoIntegrante.objects.all()
    integrantes = Integrante.objects.all()
    equipo = {}
    for tipo in tipos:
        equipo[tipo.nombre] = integrantes.filter(idTipoIntegranteRef_id=tipo.pk)
    return equipo

def index(request):
    context = {'Y': date.today().year, 'personas': equipoPorIntegrante()}
    return render(request, 'home/base.html', context)
