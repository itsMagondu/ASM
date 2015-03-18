"""
Django settings for asm project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

BASE_URL = '/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'st42b$-xzcuoi2%&fs%^v%nzkmjo!h6zgd1g6c5(42)+3gj^2z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '52.1.4.157',
    '.52.1.4.157',
    '.52.1.4.157.',
]

ADMINS = (
    ('Samuel Magondu', 'MagonduNjenga@gmail.com'), 
)

MANAGERS = ADMINS

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'siteAdmin',
    'photo',
    #'photologue',
    #'sortedm2m',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'toolbox.urls'

WSGI_APPLICATION = 'toolbox.wsgi.application'

SITE_ID = 1

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.                                            
        'NAME': 'asm',                      # Or path to database file if using sqlite3.                                                              
        'USER': 'root',                      # Not used with sqlite3.                                                                                 
        'PASSWORD': 'laFKavm6WVji',                  # Not used with sqlite3.                                                              
        'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.                                         
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.                                                    
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-uk'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = 'media/'

LOGIN_URL = BASE_URL + 'accounts/login'
LOGIN_REDIRECT_URL = BASE_URL

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'html'),
    '/opt/projects/engine/lib/python2.7/site-packages/django/contrib/admin/templates/admin',
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".                                                              
    # Always use forward slashes, even on Windows.                                                                                                    
    # Don't forget to use absolute paths, not relative paths.                                                                                         
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


