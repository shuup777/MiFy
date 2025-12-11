from django.apps import AppConfig

class UserAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'  # set to the actual package name
    verbose_name = "Manajemen Pengguna" # Nama yang muncul di Admin Panel