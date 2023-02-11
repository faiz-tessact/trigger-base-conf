#
#  Copyright (C) Tessact Pvt. Ltd. - All Rights Reserved
#  Unauthorized copying of this file, via any medium is strictly prohibited
#  Proprietary and confidential
#  Written by Faiz P <faiz@tessact.com>, January 2023
#
from .common import Common
import os


class Container(Common):
    DEBUG = True
    INSTALLED_APPS = Common.INSTALLED_APPS

    ALLOWED_HOSTS = ["*"]

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': os.environ.get('DATABASE_URL'),
            'PORT': '5432',
        }
    }
    # Cache
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://" + os.environ.get('REDIS_URL', '127.0.0.1') + ":6379",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
                "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",
            }
        }
    }
