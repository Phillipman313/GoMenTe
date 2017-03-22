from django.apps import AppConfig


class PersonasConfig(AppConfig):
    name = 'personas'

    def ready(self):
        super()
        from personas.models import crearPersona
