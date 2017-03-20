from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _

from personas.models import Persona

class PersonaInline(admin.StackedInline):
     model = Persona
     verbose_name = 'Persona'

class AdminUser(UserAdmin):
     fieldsets = (
          ('Credenciales', {'fields': ('username', 'password')}),
          (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                         'groups', 'user_permissions')}),
          (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
     )
     inlines = (PersonaInline, )
     list_display = ('username', 'is_active', 'is_staff')
     list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
     search_fields = ('username', )
     #list_display = ('username', nombre, apellido1, apellido2, identificacion)

#Register your models here.
admin.site.unregister(User)
admin.site.register(User, AdminUser)