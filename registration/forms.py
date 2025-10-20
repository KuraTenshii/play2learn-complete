# registration/forms.py
from django import forms

class CustomSignupForm(forms.Form):
    full_name = forms.CharField(max_length=100, label="Full Name")

    def signup(self, request, user):
        user.full_name = self.cleaned_data['full_name']
        user.save()
        return user
