from django.http import JsonResponse
import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import GameHistory
from reviews.models import Review

# Create your views here.
from django.views.generic import TemplateView

class MathFactsView(TemplateView):
    template_name = "math-facts.html"

class AnagramHuntView(TemplateView):
    template_name = "anagram-hunt.html"

def leaderboard(request):
    math_facts_scores = (
        GameHistory.objects.filter(game_type="math_facts")
        .order_by("-final_score", "finished_at")[:20]
    )
    anagram_scores = (
        GameHistory.objects.filter(game_type="anagram_hunt")
        .order_by("-final_score", "finished_at")[:20]
    )

    return render(request, "leaderboard.html", {
        "math_facts_scores": math_facts_scores,
        "anagram_scores": anagram_scores,
    })

@login_required
def my_game_history(request):
    histories = GameHistory.objects.filter(user=request.user)
    return render(request, "history.html", {"histories": histories})

@login_required
def math_facts_result(request):
    if request.method == "POST":
        score = int(request.POST.get("score", 0))
        settings = {
            "operation": request.POST.get("operation"),
            "max_number": request.POST.get("max_number"),
        }
        GameHistory.objects.create(
            user=request.user,
            game_type="math_facts",
            settings=settings,
            final_score=score,
        )
        return redirect("reviews:submit-review")
    return redirect("games:math-facts")

@login_required
def anagram_hunt_result(request):
    if request.method == "POST":
        score = int(request.POST.get("score", 0))
        settings = {
            "difficulty": request.POST.get("difficulty"),
            "time_limit": request.POST.get("time_limit"),
        }
        GameHistory.objects.create(
            user=request.user,
            game_type="anagram_hunt",
            settings=settings,
            final_score=score,
        )
        return redirect("reviews:submit-review")
    return redirect("games:anagram-hunt")

def home_view(request):
    reviews = Review.objects.filter(approved=True).order_by("-created_at")[:10]
    return render(request, "home.html", {"reviews": reviews})

@login_required
def submit_score(request):
    if request.method == "POST":
        data = json.loads(request.body)
        GameHistory.objects.create(
            user=request.user,
            game_type=data["game_type"],
            final_score=data["score"],
            settings=data.get("settings", {})
        )
        return JsonResponse({"status": "ok"})