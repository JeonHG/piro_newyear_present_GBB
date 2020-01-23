from django.shortcuts import render, redirect
from .forms import *
from django.db.models import Q

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
    my_game = Challenge.objects.filter(
        attacker_id=request.user.id
    ) | Challenge.objects.filter(defender_id=request.user.id)
    # my_game = Challenge.objects.filter(Q(attacker_id=request.user.id) | Q(defender_id=request.user.id))
    # https://django-orm-cookbook-ko.readthedocs.io/en/latest/query_relatedtool.html

    g = request.user

    print(g)
    context = {"games": my_game}
    return render(request, "games/game_record.html", context)


def defend(request):
    pass
