<<<<<<< HEAD
"""
WSGI config for TvNotes project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TvNotes.settings.dev')

application = get_wsgi_application()
=======
"""
WSGI config for TvNotes project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TvNotes.settings.dev')

application = get_wsgi_application()
>>>>>>> 59341e06d0b73f8d1e84f4c66dbba8b9eb9e7a91
