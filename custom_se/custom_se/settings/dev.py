from .base import *
from elasticsearch_dsl.connections import connections

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'custom_se',
        'USER': 'custom_se',
        'PASSWORD': 'custom_se',
        'HOST': 'manager-db',
        'PORT': '5432',
    }
}

connections.create_connection(hosts=['index-server-01'])
