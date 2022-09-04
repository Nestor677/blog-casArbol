from .base import *
import dajango_heroku


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = False

DEBUG_PROPAGATE_EXCEPTIONS = True
ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_pyscopg2',
        'NAME': 'd1h1d70h2n6h',
        'USER': 'ixkokltwavbsuh',
        'PASSWORD':'d350c7795bbe38e67d337a06b233833a81bd60a33be864fcbf3c40ad9893235b',
        'HOST': 'ec2-44-207-253-50.compute-1.amazonaws.com',
        'PORT':'5432',
    }
}

db_from_env= dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
django_heroku.settings(locals())

STATICFILES_STORAGE='whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_STORAGE='whitenoise.storage.CompressedStaticFilesStorage'

STATIC_URL = 'https://django-pdpostgres.herokuapp.com/static/'
MEDIA_URL = 'https://django-pdpostgres.herokuapp.com/media/'