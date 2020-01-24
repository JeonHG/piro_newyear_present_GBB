from django.urls import path, include
from core.views import home
from . import views


app_name = "pcgames"

urlpatterns = [
    # path("", home, name="main"),
    path("play/", views.create, name="play"),
    # path("processing/", views.processing, name="processing"),
    path("", views.list, name="status"),
    # path("defend/<int:game_pk>", views.defend, name="defend"),
    # path("responding/<int:game_pk>", views.finalize, name="finalize"),
    path("detail/<int:pk>", views.detail, name="detail"),
]
