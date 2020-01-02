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

DOCUMENT_MIGRATE_APPS = [
    'docs',
]

connections.create_connection(hosts=['index-server-01'])

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
