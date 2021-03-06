# Django settings for main project.
import os
import sys

DEBUG = True
APPEND_SLASH = False
TEMPLATE_DEBUG = DEBUG
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
ADMINS = ()
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'yamzam.sqlite',
    }
}
if os.environ.get('ENV', 'dev') != 'dev':
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.config(),
    }

LOGIN_URL = "/login/"
AUTH_PROFILE_MODULE = 'main.UserProfile'
TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'
FIXTURE_DIRS = (
    os.path.join(PROJECT_PATH, 'main', 'sql'),
)
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
#MEDIA_ROOT = ''
#MEDIA_URL = ''
#STATIC_ROOT = ''
STATIC_URL = '/static/'
BASE_DIR = '.'
STATICFILES_DIRS = (
    '/home/peter/dev/yamzam/app',
    os.path.join(BASE_DIR, "static"),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
SECRET_KEY = '62na=h#x3)k6m&amp;r051hw_sz-9+0(vo9239xbs6d)tf69o!)c#x'
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)
ROOT_URLCONF = 'main.urls'
WSGI_APPLICATION = 'main.wsgi.application'
TEMPLATE_DIRS = (os.path.join(PROJECT_PATH, 'templates'),)
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGINATE_BY': 10
}
LOGIN_REDIRECT_URL = '/#/profile'
SERIALIZATION_MODULES = {
    'json': 'wadofstuff.django.serializers.json'
}
INSTALLED_APPS = (
    'main',
    'rest_framework',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'worker': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'main.models': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'main.views': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
