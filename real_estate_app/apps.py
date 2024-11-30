from django.apps import AppConfig


class RealEstateAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'real_estate_app'

    def ready(self):
        import real_estate_app.signals  # Conectamos las señales

