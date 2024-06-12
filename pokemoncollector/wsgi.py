"""
WSGI config for pokemoncollector project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys

try:
    from dotenv import load_dotenv
except ImportError as e:
    sys.stderr.write(f"Error: {e}\n")
    sys.exit(1)

load_dotenv()

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pokemoncollector.settings')

application = get_wsgi_application()


from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pokemoncollector.settings")

application = get_wsgi_application()
