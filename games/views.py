from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def play(request):
    initial_data = {"attacker_id": request.user.id}
    form = ChallengeForm(initial=initial_data)
    context = {"form": form}
    return render(request, "games/create.html", context)


def processing(request):
    form = ChallengeForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.attacker_id = request.user.id
        instance.save()
        return redirect("games:status")
    else:
        pass


def status(request):
    return render(request, "games/game_record.html")
