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

