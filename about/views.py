from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import CollaborateForm
from .models import About


def about_me(request):
    """
    Renders the About page and handles collaboration requests.
    """

    about = About.objects.order_by("-updated_on").first()

    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.success(
                request,
                (
                    "Collaboration request received! "
                    "I endeavour to respond within 2 working days."
                ),
            )
            return redirect("about")  # ensure your URL name is "about"
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        collaborate_form = CollaborateForm()

    context = {
        "about": about,
        "collaborate_form": collaborate_form,
    }

    return render(request, "about/about.html", context)
