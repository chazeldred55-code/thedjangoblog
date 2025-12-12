from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    # Local apps (alphabetical)
    path("about/", include("about.urls"), name="about-urls"),
    path("", include("blog.urls"), name="blog-urls"),

    # Third-party apps
    path("accounts/", include("allauth.urls")),
    path("summernote/", include("django_summernote.urls")),

    # Django admin
    path("admin/", admin.site.urls),
]