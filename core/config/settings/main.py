import os
from pathlib import Path
import sys

from .auth import *
from .celery import *
from .database import *
from .drf import *

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent


SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    "x%#3&%giwv8f0+%r946en7z&d@9*rc$sl0qoql56xr%bh^w2mj",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]
ROOT_URLCONF = "core.config.urls"

WSGI_APPLICATION = "core.config.wsgi.application"
ASGI_APPLICATION = "core.config.asgi.application"


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "drf_spectacular",
    # first party
    "core.apps.common.apps.CommonConfig",
    "core.apps.users.apps.UsersConfig",
    "core.apps.courses.apps.CoursesConfig",
    "core.apps.steps.apps.StepsConfig",
    "core.apps.seminars.apps.SeminarsConfig",
    "core.apps.dashboard.apps.DashboardConfig",
    "core.apps.collections.apps.CollectionsConfig",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

is_running_tests = len(sys.argv) > 1 and sys.argv[1] == "test"
enable_debug_toolbar = os.getenv("ENABLE_DEBUG_TOOLBAR", "True") == "True"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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


LANGUAGE_CODE = "ru"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
AUTH_USER_MODEL = "users.CustomUser"


STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


CORS_ALLOW_ALL_ORIGINS = True
INTERNAL_IPS = ["127.0.0.1", "localhost"]

REDIS_HOST = "redis"
REDIS_PORT = "6379"
CELERY_BROKER_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"
CELERY_BROKER_TRANSPORT_OPTIONS = {"visibility_timeout": 3600}
CELERY_RESULT_BACKEND = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"
CELERYD_CONCURRENCY = 20
