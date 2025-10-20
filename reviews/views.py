from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django import forms
from .models import Review

# Create your views here.
from django.views.generic import TemplateView

class ReviewsView(TemplateView):
    template_name = "reviews.html"

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }

@login_required
def submit_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect("games:home")
    else:
        form = ReviewForm()
    return render(request, "reviews/submit_review.html", {"form": form})

def reviews_page(request):
    reviews = Review.objects.filter(featured=True)
    return render(request, "reviews/reviews.html", {"reviews": reviews})
