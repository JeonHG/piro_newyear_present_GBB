from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = "users"
urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
