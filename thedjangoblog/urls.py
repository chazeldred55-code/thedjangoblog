from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings

urlpatterns = [
    # Home (named) + /home/ alias
    path("", RedirectView.as_view(pattern_name="blog_home", permanent=False), name="home"),
    path("home/", RedirectView.as_view(pattern_name="home", permanent=False)),

    # Favicon redirect
    path(
        "favicon.ico",
        RedirectView.as_view(url=settings.STATIC_URL + "images/favicon.ico"),
        name="favicon",
    ),

    # Local apps
    path("about/", include("about.urls")),
    path("blog/", include("blog.urls")),

    # Third-party apps
    path("accounts/", include("allauth.urls")),
    path("summernote/", include("django_summernote.urls")),

    # Django admin
    path("admin/", admin.site.urls),
]