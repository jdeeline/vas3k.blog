import os
from datetime import timedelta
from pathlib import Path
from random import randint

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY") or "wow so secret"
DEBUG = (os.getenv("DEBUG") != "false")

ALLOWED_HOSTS = ["0.0.0.0", "127.0.0.1", "vas3k.blog", "vas3k.ru"]
INTERNAL_IPS = ["127.0.0.1"]

ADMINS = [
    ("vas3k", "me@vas3k.ru"),
]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "django.contrib.sitemaps",
    "authn.apps.AuthnConfig",
    "users.apps.UsersConfig",
    "posts.apps.PostsConfig",
    "comments.apps.CommentsConfig",
    "rss.apps.RssConfig",
    "inside.apps.InsideConfig",
    "clickers.apps.ClickersConfig",
    "notifications.apps.NotificationsConfig",
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "vas3k_blog.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "frontend/html",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.messages.context_processors.messages",
                "django.contrib.auth.context_processors.auth",
                "vas3k_blog.context_processors.settings_processor",
                "vas3k_blog.context_processors.cookies_processor",
            ],
        },
    },
]

WSGI_APPLICATION = "vas3k_blog.wsgi.application"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler"
        },
    },
    "loggers": {
        "": {  # "catch all" loggers by referencing it with the empty string
            "handlers": ["console"],
            "level": "DEBUG",
        },
    },
}

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("POSTGRES_DB") or "vas3k_blog_en",
        "USER": os.getenv("POSTGRES_USER") or "postgres",
        "PASSWORD": os.getenv("POSTGRES_PASSWORD") or "",
        "HOST": os.getenv("POSTGRES_HOST") or "localhost",
        "PORT": os.getenv("POSTGRES_PORT") or 5432,
    }
}

MIGRATE = os.getenv("MIGRATE")
if MIGRATE:
    DATABASES.update({
        "old": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": os.getenv("MIGRATE"),
            "USER": os.getenv("POSTGRES_USER") or "postgres",
            "PASSWORD": os.getenv("POSTGRES_PASSWORD") or "",
            "HOST": os.getenv("POSTGRES_HOST") or "localhost",
            "PORT": os.getenv("POSTGRES_PORT") or 5432,
        }
    })


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.authn.password_validation.CommonPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-US"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

STATICFILES_DIRS = [
    BASE_DIR / "frontend/static",
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Auth

CLUB_AUTH_URL = "https://vas3k.club/auth/external/"

PATREON_AUTH_URL = "https://www.patreon.com/oauth2/authorize"
PATREON_TOKEN_URL = "https://www.patreon.com/api/oauth2/token"
PATREON_USER_URL = "https://www.patreon.com/api/oauth2/v2/identity"
PATREON_CLIENT_ID = os.getenv("PATREON_CLIENT_ID")
PATREON_CLIENT_SECRET = os.getenv("PATREON_CLIENT_SECRET")
PATREON_SCOPE = "identity identity[email]"

JWT_ALGORITHM = "RS256"
JWT_PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAvEDEGKL0b+okI6QBBMiu
3GOHOG/Ml4KJ13tWyPnl5yGswf9rUGOLo0T0dXxSwxp/6g1ZeYqDR7jckuP6A3Rv
DPdKYc44eG3YB/bO2Yeq57Kx1rxvFvWZap2jTyu2wbALmmeg0ne3wkXPExTy/EQ4
LDft8nraSJuW7c+qrah+F94qKGVNvilf20V5S186iGpft2j/UAl9s81kzZKBwk7M
B+u4jSH8E3KHZVb28CVNOpnYYcLBNLsjGwZk6qbiuq1PEq4AZ5TN3EdoVP9nbIGY
BZAMwoNxP4YQN+mDRa6BU2Mhy+c9ea+fuCKRxNi3+nYjF00D28fErFFcA+BEe4A1
Hhq25PsVfUgOYvpv1F/ImPJBl8q728DEzDcj1QzL0flbPUMBV6Bsq+l2X3OdrVtQ
GXiwJfJRWIVRVDuJzdH+Te2bvuxk2d0Sq/H3uzXYd/IQU5Jw0ZZRTKs+Rzdpb8ui
eoDmq2uz6Q2WH2gPwyuVlRfatJOHCUDjd6dE93lA0ibyJmzxo/G35ns8sZoZaJrW
rVdFROm3nmAIATC/ui9Ex+tfuOkScYJ5OV1H1qXBckzRVwfOHF0IiJQP4EblLlvv
6CEL2VBz0D2+gE4K4sez6YSn3yTg9TkWGhXWCJ7vomfwIfHIdZsItqay156jMPaV
c+Ha7cw3U+n6KI4idHLiwa0CAwEAAQ==
-----END PUBLIC KEY-----"""
JWT_EXP_TIMEDELTA = timedelta(days=120)

# Email

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST", "email-smtp.eu-central-1.amazonaws.com")
EMAIL_PORT = os.getenv("EMAIL_PORT", 587)
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = "Вастрик <inside@inside.vas3k.ru>"

# Telegram

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_MAIN_CHAT_ID = os.getenv("TELEGRAM_MAIN_CHAT_ID")

# App specific

AUTH_USER_MODEL = "users.User"

SESSION_COOKIE_AGE = 300 * 24 * 60 * 60  # 300 days
SENTRY_DSN = os.getenv("SENTRY_DSN")

APP_HOST = "vas3k.blog"
MIRRORS = ["vas3k.ru"]

CSRF_TRUSTED_ORIGINS = [
    "https://vas3k.blog",
    "https://*.vas3k.blog",
    "https://vas3k.ru",
    "https://*.vas3k.ru",
]

AUTHOR = "@vas3k"
TITLE = "vas3k"
DESCRIPTION = "Personal blog about technology and survival in the world of cyberpunk"

STYLES_HASH = os.getenv("GITHUB_SHA") or str(randint(1, 10000))

MAX_COMMENTS_PER_24H = 50
