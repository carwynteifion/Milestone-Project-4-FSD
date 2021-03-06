from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Subscriber

# Create your views here.


def index(request):
    """View to return the index page"""
    return render(request, "home/index.html")


def error_404(request, exception):
    """Returns 404 page"""
    return render(request, "404.html", status=404)


def error_403(request, exception):
    """Returns 403 page"""
    return render(request, "403.html", status=403)


def error_400(request, exception):
    """Returns 400 page"""
    return render(request, "400.html", status=400)


def error_500(request):
    """Returns 500 page"""
    return render(request, "500.html", status=500)


def subscribe(request):
    """
    Adds subscribed user to mailing list
    """
    email = request.POST.get("email")
    privacy = request.POST.get("privacy") == "on"
    redirect_url = "/"

    subscriber = Subscriber(email=email, privacy=privacy)
    duplicate = Subscriber.objects.filter(email=email)
    if not duplicate:
        subscriber.save()
        messages.info(
            request, 'Subscribed to newsletter', extra_tags='newsletter'
        )
    else:
        messages.error(
            request, f'Email {email} is already subscribed to the newsletter',
            extra_tags='newsletter'
        )
    return redirect(redirect_url)
