from datetime import date

from django.shortcuts import render

# Create your views here.
from photologue.models import Gallery

from home.models import TipoIntegrante, Integrante, Acerca
from programas.models import Programa


def sobre():
    return Acerca.objects.all().first()

def equipoPorIntegrante():
    tipos = TipoIntegrante.objects.all()
    integrantes = Integrante.objects.all()
    equipo = {}
    for tipo in tipos:
        equipo[tipo.nombre] = integrantes.filter(idTipoIntegranteRef_id=tipo.pk)
    return equipo

def programa():
    return Programa.objects.all()

def index(request):
    context = {'Y': date.today().year, 'sobre': sobre(), 'personas': equipoPorIntegrante(), 'eventos': programa()}
    return render(request, 'home/base.html', context)

def galeria(request):
    albumes = Gallery.objects.all()
    context = {'fotos': albumes}
    return render(request, 'home/galeria.html', context)
