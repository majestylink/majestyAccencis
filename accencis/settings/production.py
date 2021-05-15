from .base import *
import dj_database_url

os.environ['SECRET_KEY'] = '-3lb1e&1l+x!(f10t=+dyzjo=zjdknex1sgemqbaz5#fgglac#'
SECRET_KEY = os.environ['SECRET_KEY'] 
DEBUG = True #TODO: Turn off on realease
# DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS += ["accencis.biz", "accencis.com.ng"]

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'accencisdb',
        'USER': 'accencis',
        'PASSWORD': 'Pass@1234',
        'HOST': 'localhost',
        'PORT': '',
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite3'),
#     }
# }
DATABASES_URL = os.environ['DATABASE_URL'] 
#
DATABASES['default'] = dj_database_url.parse(DATABASES_URL, conn_max_age=600)


STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/accencisstatic/'
# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)
MEDIA_URL = '/accencismedia/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

HOST = "https://accencis.biz"

# Google cloud for images
DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_PROJECT_ID ='accencis'
GS_BUCKET_NAME = 'accencis'
GS_FILE_OVERWRITE = True
from google.oauth2 import service_account
GS_AUTH_FILE = os.path.join(PROJECT_ROOT, "accencis-44afd28677af.json")
GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
    GS_AUTH_FILE)