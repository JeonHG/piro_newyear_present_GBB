from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from .models import Pcgame
from .forms import PcgameForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
import random


class DetailView(DetailView):
    model = Pcgame
    context_object_name = "pcgame"
    template_name = "pcgames/detail.html"

    def get_context_data(self, **kwargs):
        """Insert the single object into the context dict."""
        context = {}
        if self.object:
            context["object"] = self.object
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(kwargs)
        return super().get_context_data(**context)


detail = DetailView.as_view()


class ListView(ListView):
    model = Pcgame
    context_object_name = "pcgames"
    template_name = "pcgames/list.html"


list = ListView.as_view()


class CreateView(CreateView):
    model = Pcgame
    form_class = PcgameForm
    template_name = "pcgames/create.html"
    success_url = reverse_lazy("pcgames:status")

    def form_valid(self, form):
        pc_random = random.randint(0, 2)
        form.instance.computer_choice_id = pc_random
        form.instance.winner = self.get_winner(form.instance.human_choice_id, pc_random)
        return super().form_valid(form)

    # https://docs.djangoproject.com/en/3.0/topics/class-based-views/generic-editing/

    def get_winner(self, human_choice, computer_choice):
        delta = human_choice - computer_choice
        if delta == 1 or delta == -2:
            return True
        elif delta == 0:
            return None
        else:
            return False


create = CreateView.as_view()
