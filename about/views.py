from django.shortcuts import render
from .models import About
from .forms import CollaborateForm


def about_me(request):
    # Get the latest About content
    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    context = {
        "about": about,
        "collaborate_form": collaborate_form,
    }

    return render(request, "about/about.html", context)