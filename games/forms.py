from django import forms
from .models import *


class ChallengeForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = ("defender", "attacker_choice")

