from django.shortcuts import render
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
    else:
        pass
