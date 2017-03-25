from datetime import date

from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'Y': date.today().year}
    return render(request, 'home/index.html', context)