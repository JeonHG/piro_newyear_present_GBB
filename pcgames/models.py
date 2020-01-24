from django.db import models
from core import models as core_models
from games import models as games_models


class Pcgame(core_models.TimeStampedModel):
    human_choice = models.ForeignKey(
        games_models.Weapon,
        related_name="human_choice",
        on_delete=models.SET_NULL,
        null=True,
    )
    computer_choice = models.ForeignKey(
        games_models.Weapon,
        related_name="_choice",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    winner = models.BooleanField(
        blank=True, null=True
    )  # True for human win, False for computer win

    def __str__(self):
        return f"{self.id} - 컴퓨터 vs 인간"

