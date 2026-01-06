from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

from django.shortcuts import render, redirect
from .models import ContactMessage

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Save to database
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        # Optionally, redirect to a "success" page
        return redirect("contact_us:success")

    return render(request, "contact/contact-us.html")


def success_view(request):
    return render(request, 'contact/success.html')
