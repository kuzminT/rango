# coding: utf-8
import os
from options import *

"""
Django settings for tango_with_django_project project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gi-0k7i5204i1v^+&j2m9i34jc8p0)nwbi^#jo-(+!u7^xdulz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['rango.loc']

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

STATIC_DIR = os.path.join(BASE_DIR, 'static/')

STATIC_ROOT = os.path.join(BASE_DIR, "static/")

MEDIA_DIR = os.path.join(BASE_DIR, 'media/')

ROOT_URLCONF = 'tango_with_django_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR, ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'context_processors.user_ip.user_ip'
            ],
        },
    },
]


STATIC_URL = '/static/'

STATICFILES_DIRS = [STATIC_DIR, MEDIA_DIR]

STATICFILES_FINDERS =  ('compressor.finders.CompressorFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
                        )

ADMIN_MEDIA_PREFIX = '/static/admin/'

MEDIA_ROOT = MEDIA_DIR

MEDIA_URL = '/media/'

WSGI_APPLICATION = 'tango_with_django_project.wsgi.application'
