from django.urls import path
from games.views import GameView, ResultPageView

urlpatterns = [
    path('', GameView.as_view(), name='game'),
    path('result/', ResultPageView.as_view(), name='result'),
]
