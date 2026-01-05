from django.urls import path

from games.views import (
    MathFactsView,
    AnagramHuntView, 
    home_view, 
    leaderboard, 
    my_game_history, 
    math_facts_result, 
    anagram_hunt_result,
    submit_score
)

urlpatterns = [
    path('', home_view, name='home'),
    path('math-facts/', MathFactsView.as_view(), name='math-facts'),
    path('anagram-hunt/', AnagramHuntView.as_view(), name='anagram-hunt'),
    path("math-facts/result/", math_facts_result, name="math-facts-result"),
    path("anagram-hunt/result/", anagram_hunt_result, name="anagram-hunt-result"),
    path("leaderboard/", leaderboard, name="leaderboard"),
    path("history/", my_game_history, name="my-history"),
    path("submit-score/", submit_score, name="submit-score"),
]