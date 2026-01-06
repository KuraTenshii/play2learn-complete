from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from games.models import GameHistory

GAME_DISPLAY_NAMES = {
    "math_facts": "Math Facts",
    "anagram_hunt": "Anagram Hunt",
}

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
        "game_name": GAME_DISPLAY_NAMES.get(game_type, game_type.replace("_", " ").title()),
    })
