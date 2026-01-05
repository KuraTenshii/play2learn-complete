from django.urls import path
from .views import leaderboard

urlpatterns = [
    path("leaderboard/<str:game_type>/", leaderboard, name="leaderboard"),
]