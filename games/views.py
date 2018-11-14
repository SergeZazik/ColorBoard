from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from games.forms import GameForm
from games.models import GameResult
from utils.calculation import game_calculation

# Create your views here.


class GameView(FormView):
    template_name = 'game.html'
    form_class = GameForm
    success_url = '/result/'

    def form_valid(self, form):
        game_calculation(**form.cleaned_data)
        return super(GameView, self).form_valid(form)


class ResultPageView(TemplateView):

    template_name = "result.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_result'] = GameResult.objects.last()
        return context
