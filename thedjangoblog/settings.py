import os
from pathlib import Path
from decouple import config
import dj_database_url

# Load env.py if present (local development)
if os.path.isfile("env.py"):
    import env

# ------------------------
# Paths
# ------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"
MEDIA_DIR = BASE_DIR / "media"

# ------------------------
# Security
# ------------------------
SECRET_KEY = config("SECRET_KEY", default="unsafe-secret-key")

# DEBUG = False on Heroku, True locally
DEBUG = config("DEBUG", default=True, cast=bool)

ALLOWED_HOSTS = [
    "thedjangoblog.herokuapp.com",
    ".herokuapp.com",
    "localhost",
    "127.0.0.1",
]

# REQUIRED for Heroku
CSRF_TRUSTED_ORIGINS = [
    "https://thedjangoblog.herokuapp.com",
]

# ------------------------
# Installed apps
# ------------------------
INSTALLED_APPS = [

    # Django default apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",

    # Third-party apps
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "django_summernote",

    # Local apps
    "about",
    "blog",
]

SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# ------------------------
# Middleware
# ------------------------
MIDDLEWARE = [
    # Security
    "django.middleware.security.SecurityMiddleware",

    # Static files (must come immediately after SecurityMiddleware)
    "whitenoise.middleware.WhiteNoiseMiddleware",

    # Django core middleware
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    # Third-party middleware
    "allauth.account.middleware.AccountMiddleware",
]

# ------------------------
# URL Config
# ------------------------
ROOT_URLCONF = "thedjangoblog.urls"

# ------------------------
# Templates
# ------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATES_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "thedjangoblog.wsgi.application"

# ------------------------
# Database
# ------------------------
DATABASES = {
    "default": dj_database_url.config(
        default=config("DATABASE_URL", default="sqlite:///db.sqlite3"),
        conn_max_age=600,
        ssl_require=not DEBUG,  # ssl only on heroku
    )
}

# ------------------------
# Password validation
# ------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

ACCOUNT_EMAIL_VERIFICATION = 'none'

# ------------------------
# Internationalization
# ------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ------------------------
# Static files
# ------------------------
STATIC_URL = "/static/"

STATICFILES_DIRS = [STATIC_DIR] if DEBUG else []

STATIC_ROOT = BASE_DIR / "staticfiles"

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# ------------------------
# Media files
# ------------------------
MEDIA_URL = "/media/"
MEDIA_ROOT = MEDIA_DIR

# ------------------------
# Summernote (optional defaults)
# ------------------------
X_FRAME_OPTIONS = "SAMEORIGIN"

SUMMERNOTE_CONFIG = {
    "iframe": True,
    "summernote": {
        "width": "100%",
        "height": "300",
    },
}

# ------------------------
# Default Auto Field
# ------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"