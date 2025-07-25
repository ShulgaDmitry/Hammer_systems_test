"""
WSGI config for setting project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

# import os
#
# from django.core.wsgi import get_wsgi_application
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setting.settings')
#
# application = get_wsgi_application()


import os
import sys

path = '/home/dmitry161992/Hammer_systems_test'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setting.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()