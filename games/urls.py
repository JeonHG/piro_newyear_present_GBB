from django.urls import path, include
from core.views import home
from .views import gameForm

app_name = "games"

urlpatterns = [
    path("", home, name="main"),
    path("start/", gameForm, name="gameForm"),
]

