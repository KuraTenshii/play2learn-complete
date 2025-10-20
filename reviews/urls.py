from django.urls import path

# Create your views here.
from reviews.views import ReviewsView, submit_review, reviews_page

urlpatterns = [
    path('reviews/', ReviewsView.as_view(), name='reviews'),
    path("submit/", submit_review, name="submit-review"),
    path("", reviews_page, name="reviews"),
]