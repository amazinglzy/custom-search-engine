"""
WSGI config for custom_se project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'custom_se.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'custom_se.settings.{os.environ.get("CUSTOM_MODE", "dev")}')

application = get_wsgi_application()
