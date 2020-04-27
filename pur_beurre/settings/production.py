from . import *

import os
import logging

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import LoggingIntegration


sentry_logging = LoggingIntegration(
    level=logging.INFO,        # Capture info and above as breadcrumbs
    event_level=logging.INFO   # Send errors as events
)

sentry_sdk.init(
    dsn="https://c42d683c1779454f9b50c0e420af723a@o380264.ingest.sentry.io"
        "/5205889",
    integrations=[DjangoIntegration(), sentry_logging],

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)


SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = ['178.62.10.30']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pur_beurre_db',
        'USER': 'ebarbier',
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': '',
        'PORT': '5432',
    }
}
