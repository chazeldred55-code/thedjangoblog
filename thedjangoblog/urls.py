from django.contrib import admin
from django.urls import path, include  # include allows app-level URL routing

urlpatterns = [
    # About page first
    path("about/", include("about.urls"), name="about-urls"),

    # Django admin
    path("admin/", admin.site.urls),

    # Summernote editor
    path("summernote/", include("django_summernote.urls")),

    # All blog-related routes handled in blog/urls.py
    path("", include("blog.urls"), name="blog-urls"),
]
