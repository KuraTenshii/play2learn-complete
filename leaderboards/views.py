from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from games.models import GameHistory

@login_required
def leaderboard(request, game_type):
    scores = (
        GameHistory.objects
        .filter(game_type=game_type)
        .select_related("user")
        .order_by("-final_score", "finished_at")[:25]
    )

    return render(request, "leaderboard.html", {
        "scores": scores,
        "game_type": game_type,
    })