import os
import urlparse

from django.utils.crypto import get_random_string

import dj_database_url
from boto.s3.connection import OrdinaryCallingFormat

from kiroletik.settings import * #noqa


DEBUG = False

DATABASES['default'] = dj_database_url.config()


###########
# Storage #
###########

INSTALLED_APPS += ['storages']

AWS_S3_HOST = 's3.us.archive.org'
AWS_S3_USE_SSL = False
AWS_STORAGE_BUCKET_NAME = 'kiroletik'
AWS_AUTO_CREATE_BUCKET = True
AWS_S3_CALLING_FORMAT = OrdinaryCallingFormat()
AWS_S3_CUSTOM_DOMAIN = 'https://{}.s3.us.archive.org'.format(
    AWS_STORAGE_BUCKET_NAME)

DEFAULT_FILE_STORAGE = 'herokuify.storage.S3BotoStorage'
COMPRESS_STORAGE = 'herokuify.storage.CachedS3StaticStorage'


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
CSRF_COOKIE_SECURE = True

ALLOWED_HOSTS = ['kiroletik.herokuapp.com',
                 'kiroletik.eus',
                 'www.kiroletik.eus']

#############
# Memcached #
#############

CACHES = {
    'default': {
        'BACKEND': 'django_bmemcached.memcached.BMemcached',
        'LOCATION': os.environ.get('MEMCACHEDCLOUD_SERVERS').split(','),
        'OPTIONS': {
            'username': os.environ.get('MEMCACHEDCLOUD_USERNAME'),
            'password': os.environ.get('MEMCACHEDCLOUD_PASSWORD')
        }
    }
}


#########
# Redis #
#########

redis_url = urlparse.urlparse(os.environ.get('REDISCLOUD_URL'))

SESSION_ENGINE = 'redis_sessions.session'
SESSION_REDIS_HOST = redis_url.hostname
SESSION_REDIS_PORT = redis_url.port
SESSION_REDIS_PASSWORD = redis_url.password


########
# SMTP #
########

ADMINS = [
    ('Unai Zalakain', 'contact@unaizalakain.info'),
]

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('SENDGRID_USERNAME')
EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_PASSWORD')
EMAIL_USE_TLS = True
SERVER_EMAIL = 'system@kiroletik.eus'
EMAIL_SUBJECT_PREFIX = '[Kiroletik] '

###########
# Logging #
###########

MIDDLEWARE_CLASSES += [('rollbar.contrib.django.'
                        'middleware.RollbarNotifierMiddleware')]

ROLLBAR = {
    'access_token': 'df66058b7a7d41d1965bba4a48b5eac0',
    'environment': 'development' if DEBUG else 'production',
    'branch': 'master',
    'root': BASE_DIR,
}

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
