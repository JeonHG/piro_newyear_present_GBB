from django import forms
from .models import *
from users.models import User


class ChallengeForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = ("defender", "attacker_choice")

    def __init__(self, *args, **kwargs) -> object:
        super(ChallengeForm, self).__init__(*args, **kwargs)
        try:
            kwargs["initial"]
            self.fields["defender"].queryset = User.objects.all().exclude(
                id=kwargs["initial"]["attacker_id"]
            )
        except KeyError:
            pass


class DefendForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = ("defender", "defender_choice")

    def __init__(self, *args, **kwargs) -> object:
        super(DefendForm, self).__init__(*args, **kwargs)
        try:
            target_game = kwargs["initial"]["game"]
            self.fields["defender"].queryset = User.objects.filter(
                id=target_game.defender.id
            )
            self.fields["defender"].initial = target_game.defender
        except KeyError:
            pass
