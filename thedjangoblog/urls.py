from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings

urlpatterns = [
    # Favicon redirect
    path(
        "favicon.ico",
        RedirectView.as_view(url=settings.STATIC_URL + "images/favicon.ico"),
        name="favicon",
    ),

    # Local apps (alphabetical)
    path("about/", include("about.urls"), name="about-urls"),
    path("", include("blog.urls"), name="blog-urls"),

    # Third-party apps
    path("accounts/", include("allauth.urls")),
    path("summernote/", include("django_summernote.urls")),

    # Django admin
    path("admin/", admin.site.urls),
]
