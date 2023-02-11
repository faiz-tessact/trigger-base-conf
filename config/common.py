#
#  Copyright (C) Tessact Pvt. Ltd. - All Rights Reserved
#  Unauthorized copying of this file, via any medium is strictly prohibited
#  Proprietary and confidential
#  Written by Faiz P <faiz@tessact.com>, January 2023
#
import os
from os.path import join

from configurations import Configuration, values
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BACKEND_URL = os.getenv("BACKEND", '127.0.0.1')
FRONTEND_URL = os.getenv("FRONTEND", '127.0.0.1')

class Common(Configuration):

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    DEBUG = values.BooleanValue(True)

    INSTALLED_APPS = [
        #default apps
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        #rest framework
        'rest_framework',

        #project apps
        'library',

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

    ROOT_URLCONF = 'urls'

    SECRET_KEY = 'django-insecure-ho@t*py)wg(x5q3h44x0bltmiu@v_iylxum4i*4c#4gqe82c1m'

    WSGI_APPLICATION = 'wsgi.application'

    # Local db
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': join(BASE_DIR, 'db.sqlite3'),
        }
    }

    TIME_ZONE = 'UTC'

    LANGUAGE_CODE = 'en-us'

    # If you set this to False, Django will make some optimizations so as not
    # to load the internationalization machinery.
    USE_I18N = False
    USE_L10N = True
    USE_TZ = True
    LOGIN_REDIRECT_URL = '/'

    # Static Files
    STATIC_ROOT = join(BASE_DIR, 'staticfiles')

    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )

    # Local media files
    MEDIA_ROOT = join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            'OPTIONS': {
                'context_processors': [
                    'django.contrib.auth.context_processors.auth',
                    'django.template.context_processors.debug',
                    'django.template.context_processors.i18n',
                    'django.template.context_processors.media',
                    'django.template.context_processors.static',
                    'django.template.context_processors.request',
                    'django.template.context_processors.tz',
                    'django.contrib.messages.context_processors.messages'
                ],
                'loaders': [
                    ('django.template.loaders.cached.Loader', [
                        'django.template.loaders.filesystem.Loader',
                        'django.template.loaders.app_directories.Loader',
                    ]),
                    # 'admin_tools.template_loaders.Loader',
                ],
                'libraries': {
                    'staticfiles': 'django.templatetags.static',
                }
            },
        },
    ]


    STATIC_URL = 'static/'
