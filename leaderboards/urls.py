from django.urls import path

from leaderboards.views import LeaderboardsView

urlpatterns = [
    path('leaderboards/', LeaderboardsView.as_view(), name='leaderboard'),
]
