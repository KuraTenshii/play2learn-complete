from django.shortcuts import render

from django.views.generic import TemplateView

class LeaderboardsView(TemplateView):
    template_name = "leaderboard.html"
