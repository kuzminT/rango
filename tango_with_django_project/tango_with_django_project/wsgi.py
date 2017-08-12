"""
WSGI config for tango_with_django_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""
from __future__ import unicode_literals

# import sys

import os

# DJANGO_PATH =  os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', '..', '..')
# sys.path.append(DJANGO_PATH)

# settings_module = "%s.settings" % PROJECT_ROOT.split(os.sep)[-1]
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tango_with_django_project.settings")

application = get_wsgi_application()

# print(os.environ['VIRTUAL_ENV'])
