from django import forms
from .models import *


class PcgameForm(forms.ModelForm):
    class Meta:
        model = Pcgame
        fields = ("human_choice",)

