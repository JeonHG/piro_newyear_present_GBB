from django.urls import path, include
from core.views import home
from . import views


app_name = "games"

urlpatterns = [
    path("", home, name="main"),
    path("play/", views.play, name="play"),
    path("processing/", views.processing, name="processing"),
    path("status/", views.status, name="status"),
    path("defend/<int:game_pk>", views.defend, name="defend"),
    path("responding/<int:game_pk>", views.finalize, name="finalize"),
    path("detail/<int:game_pk>", views.detail, name="detail"),
]

