from django.urls import path
from . import views

# provide an app namespace so templates can use the 'admin:...' names
app_name = 'admin'

urlpatterns = [
    path("login/", views.admin_login_view, name="admin_login"),
    path("dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("logout/", views.admin_logout_view, name="admin_logout"),
]
