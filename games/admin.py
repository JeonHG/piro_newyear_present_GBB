from django.contrib import admin
from . import models


@admin.register(models.Challenge)
class GameAdmin(admin.ModelAdmin):
    list_display = ("__str__", "attacker", "defender", "get_winner")


@admin.register(models.Weapon)
class WeaponAdmin(admin.ModelAdmin):
    list_display = ("name",)
