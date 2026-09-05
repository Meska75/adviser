from adviserwebsite.settings import *
import dj_database_url
import os

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")
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

# فقط وقتی سایت روی HTTPS کامل کار می‌کند اینها را فعال کن
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# طول مدت HSTS — ابتدا مقدار کمتری برای تست، بعد از مطمئن شدن مقدار را افزایش دهید
SECURE_HSTS_SECONDS = 3600   # ابتدا تستی: 3600 (یک ساعت) — بعد از اطمینان افزایش بدید
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True  # ابتدا False؛ وقتی مطمئن شدی True کن و ثبت انجام بده