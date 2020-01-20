from django.urls import path, include
from core.views import home
from .views import gameForm, gameRecord

app_name = "games"

urlpatterns = [
    path("", home, name="main"),
    path("start/", gameForm, name="gameForm"),
    path("game-record", gameRecord, name="gameRecord"),
]

