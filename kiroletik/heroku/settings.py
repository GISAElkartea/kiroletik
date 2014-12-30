from django.utils.crypto import get_random_string

import dj_database_url

from kiroletik.settings import * #noqa

DEBUG = False

DATABASES['default'] = dj_database_url.config()

#####################
# Security settings #
#####################

SECRET_KEY = os.environ.get('SECRET_KEY', get_random_string(
    50, 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'))

INSTALLED_APPS += ['djangosecure']

MIDDLEWARE_CLASSES += ['djangosecure.middleware.SecurityMiddleware']
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 60*60*24
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_FRAME_DENY = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True

ALLOWED_HOSTS = ['kiroletik.herokuapp.com',
                 'kiroletik.eus',
                 'www.kiroletik.eus']

#################
# Static assets #
#################

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

###########
# Logging #
###########

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
        }
    }
}