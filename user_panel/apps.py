from django.apps import AppConfig


class UserPanelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_panel'

    def ready(self):
        # Call signal registration functions
        import user_panel.signals
