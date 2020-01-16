from django.db import models
from core import models as core_models
from users.models import User


class Weapon(models.Model):

    """ Weapon model definition"""

    SCISSORS = 0
    ROCK = 1 
    PAPER = 2
    NAME_CHOICES = (
        (SCISSORS, "가위"),
        (ROCK, "바위"),
        (PAPER, "보"),
    )

    name = models.IntegerField(choices=NAME_CHOICES)

    def __str__(self):
        if self.name == 0:
            return "가위"
        elif self.name == 1:
            return "바위"
        else:
            return "보"


class Challenge(core_models.TimeStampedModel):

    """challenge model definition"""

    attacker = models.ForeignKey(User, related_name="attacker", on_delete=models.SET_NULL, null=True)
    defender = models.ForeignKey(User, related_name="defender", on_delete=models.SET_NULL, null=True)
    attacker_choice = models.ForeignKey(
        Weapon, related_name="pc_choice", on_delete=models.SET_NULL, null=True
    )
    defender_choice = models.ForeignKey(
        Weapon, related_name="human_choice", on_delete=models.SET_NULL, null=True, blank=True
    )
    winner = models.ForeignKey(User, related_name="winner", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.id} - {self.attacker} vs {self.defender}'

    def get_winner(self):
        if self.attacker_choice and self.defender_choice:
            delta = self.attacker_choice.name - self.defender_choice.name
            if delta == 1 or delta == -2:
                return self.attacker
            elif delta == 0:
                return "무승부"
            else:
                return self.defender
        else:
            return "경기중"
    get_winner.short_description = "winner"
