from adviserwebsite.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dB_zE60ul5prm_HNKF09NACwOfb-9AoAvyOpWxGIoyPpv6g04P0S-EqTDTao3tdARTIQ'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =False
ALLOWED_HOSTS = ["*"]

# INSTALLED_APPS = []

SITE_ID = 1


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

MEDIA_URL = '/media/'
MEDIA_ROOT = "media"

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]
