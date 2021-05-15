import os
from decouple import config
import dj_database_url
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
# SECRET_KEY = config('SECRET_KEY')
SECRET_KEY = "3pt+_sm2@+r7d48cy^3()*uic_+lu7cz6q$*vo-cr@94-3&%ll"
ALLOWED_HOSTS = ['127.0.0.1',]
INSTALLED_APPS = [
    'jet.dashboard',
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',
    'django_countries',
    'import_export',
    'ckeditor',
    'ckeditor_uploader',
    'tinymce',
    'storages',

    'core',
    'shop',
    'audience',
    'blog',
    'gallery',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'accencis.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_ROOT, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'core.core_context.UniversalContext',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'accencis.wsgi.application'
#AUTH_USER_MODEL='accounts.User'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Lagos'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Auth
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
)
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True

#  Mail sending 
# SERVER_EMAIL = 'info@accencis.biz'
SERVER_EMAIL = 'majestyempirebiz@gmail.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_SSL = True
EMAIL_PORT = 465
EMAIL_HOST_USER = 'majestyempirebiz@gmail.com'
# EMAIL_HOST_PASSWORD = os.environ['EMAIL_PASS']
EMAIL_HOST_PASSWORD = 'veronsvhtvcsltqr'

DEFAULT_FROM_EMAIL = 'ACCENCIS.BIZ <info@accencis.biz>'
# Custom Config
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/' 
APPEND_SLASH = True
IMPORT_EXPORT_USE_TRANSACTIONS = True
# CRISPY FORMS
CRISPY_TEMPLATE_PACK = 'bootstrap4'
CKEDITOR_UPLOAD_PATH = "ck/uploads/"
X_FRAME_OPTIONS = 'SAMEORIGIN'
