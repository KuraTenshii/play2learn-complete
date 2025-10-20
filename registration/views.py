# Create your views here.
from django.shortcuts import render

from django.views.generic import TemplateView

class UserAccount(TemplateView):
    template_name = "account/my_account.html"