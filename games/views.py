from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.db.models import Q
from django.http import Http404
from django.forms.models import model_to_dict
from django.views.generic import DetailView


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


def finalize(request, game_pk):
    game = get_object_or_404(Challenge, id=game_pk)
    if game.defender_id == request.user.id:
        form = DefendForm(request.POST)
        if form.is_valid():
            game.defender_choice = form.cleaned_data["defender_choice"]
            delta = game.attacker_choice.name - game.defender_choice.name
            # print(delta)
            if delta == 1 or delta == -2:
                game.winner = game.attacker
            elif delta == 0:
                pass
            else:
                game.winner = game.defender
            game.save()
        # game.defender_choice = request.POST
        return redirect("games:status")
    else:
        return None


def status(request):
    my_games = Challenge.objects.filter(
        attacker_id=request.user.id
    ) | Challenge.objects.filter(defender_id=request.user.id)
    # my_game = Challenge.objects.filter(Q(attacker_id=request.user.id) | Q(defender_id=request.user.id))
    # https://django-orm-cookbook-ko.readthedocs.io/en/latest/query_relatedtool.html
    context = {"games": my_games.order_by("id")}
    return render(request, "games/game_record.html", context)


def defend(request, game_pk):
    game = get_object_or_404(Challenge, id=game_pk)
    if game.defender_id == request.user.id:
        initial_data = {"game": game}
        form = DefendForm(initial=initial_data)
        context = {"form": form, "game": game}
        return render(request, "games/update.html", context)
    else:
        raise Http404


def detail(request, game_pk):
    game = get_object_or_404(Challenge, id=game_pk)
    print(model_to_dict(game))
    context = {"game": model_to_dict(game)}
    return render(request, "games/detail.html", context)


class DetailView(DetailView):
    def get(self, request, *args, **kwargs):
        game = get_object_or_404(Challenge, pk=kwargs["game_pk"])
        context = {"game": game}
        return render(request, "games/detail.html", context)


detail = DetailView.as_view()
