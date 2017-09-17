# coding: utf-8
from apps import *
from caches import *
from auth import *

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME': 'rango',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': ''
    }
}