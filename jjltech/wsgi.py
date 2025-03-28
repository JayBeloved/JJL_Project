"""
WSGI config for jjltech project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jjltech.settings')
if os.getenv('ENV') == 'production':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jjltech.settings.production')

application = get_wsgi_application()
