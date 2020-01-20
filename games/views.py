from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def play(request):
    form = ChallengeForm()
    context = {"form": form}
    return render(request, "games/create.html", context)


def processing(request):
    print(request.POST)
    form = ChallengeForm(request.POST)
    if form.is_valid():
        form.save()
        print(form.save())
        return redirect("games:status")
    else:
        pass


def status(request):
    return render(request, "games/game_record.html")
