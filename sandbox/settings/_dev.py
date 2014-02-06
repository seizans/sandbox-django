# coding=utf8
# 開発用の環境で共通の設定
# base系の後で import * されるので、上書きをする挙動になる

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n+i_fly3y8v%(hgp#n(9h3@brw6qjiae)$gauqd)mee1t3dp1u'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


INSTALLED_APPS_PLUS = (
    'debug_toolbar',
)
