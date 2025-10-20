from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                subject=f'Contact Us Message from {name}',
                message=f'From: {name} <{email}>\n\n{message}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
            return redirect('contact-us-success')
    else:
        form = ContactForm()
    
    return render(request, 'contact/contact-us.html', {'form': form})

def success_view(request):
    return render(request, 'contact/contact-us-success.html')
