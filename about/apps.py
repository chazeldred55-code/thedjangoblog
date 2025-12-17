from django.apps import AppConfig


class AboutConfig(AppConfig):
    """
    App configuration for the About app.
    Sets the default primary key field type.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about'
