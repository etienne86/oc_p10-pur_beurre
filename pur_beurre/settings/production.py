from . import *

import os

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
