from django.shortcuts import render
from .models import About

def about_me(request):
    # Get the latest About content
    about = About.objects.all().order_by('-updated_on').first()
    return render(request, "about/about.html", {"about": about})