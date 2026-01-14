from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings

urlpatterns = [
    # Home
    path("", RedirectView.as_view(pattern_name="blog_home", permanent=False), name="home"),
    
    path("favicon.ico", RedirectView.as_view(url=settings.STATIC_URL + "images/favicon.ico"), name="favicon"),

    path("about/", include("about.urls")),
    path("blog/", include("blog.urls")),  # homepage now at /blog/

    path("accounts/", include("allauth.urls")),
    path("summernote/", include("django_summernote.urls")),
    path("admin/", admin.site.urls),

    # Redirect / to /blog/ so homepage works
    path("", RedirectView.as_view(url="/blog/", permanent=False)),
]
