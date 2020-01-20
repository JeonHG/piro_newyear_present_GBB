from django.shortcuts import render
from .forms import *

# Create your views here.
def gameForm(request):
    if request.method == "POST":
        form = ChallengeForm(request.POST)
        if form.is_valid():
            game = form.save()
            return redirect("games:main", game.id)
        return redirect("games:main")
    else:
        form = ChallengeForm()
        return render(request, "games/create.html", {"form": form})


def gameRecord(request):
    return render(request, "games/game_record.html")

