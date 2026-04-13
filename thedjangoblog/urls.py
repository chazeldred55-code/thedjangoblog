from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views  # ✅ added

urlpatterns = [
    # Home (named) + /home/ alias
    path(
        "",
        RedirectView.as_view(
            pattern_name="blog_home",
            permanent=False,
        ),
        name="home",
    ),
    path(
        "home/",
        RedirectView.as_view(
            pattern_name="home",
            permanent=False,
        ),
    ),

    # Favicon redirect
    path(
        "favicon.ico",
        RedirectView.as_view(
            url=settings.STATIC_URL + "images/favicon.ico",
        ),
        name="favicon",
    ),

    # Local apps
    path("about/", include("about.urls")),
    path("blog/", include("blog.urls")),

    # 🔐 Password reset (Django built-in)
    path(
        "accounts/password_reset/",
        auth_views.PasswordResetView.as_view(),
        name="password_reset",
    ),
    path(
        "accounts/password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "accounts/reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "accounts/reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),

    # Third-party apps (keep AFTER custom overrides if needed)
    path("accounts/", include("allauth.urls")),
    path("summernote/", include("django_summernote.urls")),

    # Django admin
    path("admin/", admin.site.urls),
]