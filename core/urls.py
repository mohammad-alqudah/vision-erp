from django.urls import path

from . import views
from .auth_views import LoginView, LogoutView

urlpatterns = [
    path("health/", views.health, name="health"),
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),
]


