from django.urls import path

from registration.views import UserAccount

urlpatterns = [
  path('my_account/', UserAccount.as_view(), name='user_account'),
]
