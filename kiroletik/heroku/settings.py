from django.utils.crypto import get_random_string

import dj_database_url

from kiroletik.settings import * #noqa

DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY', get_random_string(
    50, 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'))

DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['kiroletik.herokuapp.com',
                 'kiroletik.eus',
                 'www.kiroletik.eus']

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'


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
