from django.contrib import admin

# Register your models here.
from home.models import TipoIntegrante, Integrante, Tercero, Acerca

admin.site.register(TipoIntegrante)
admin.site.register(Integrante)
admin.site.register(Tercero)
admin.site.register(Acerca)