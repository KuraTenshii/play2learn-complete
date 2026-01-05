from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm

@login_required
def submit_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.approved = True
            review.save()
            return redirect("games:home")
    else:
        form = ReviewForm()
    return render(request, "reviews/submit_review.html", {
        "form": form
    })
