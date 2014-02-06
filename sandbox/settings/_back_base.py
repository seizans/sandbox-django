# coding=utf8
# backアプリケーション(管理用)に共通の設定
from ._base import *  # NOQA

ROOT_URLCONF = 'core.back_urls'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # 管理アプリではブラウザ閉じるとセッション期限切れにする

INSTALLED_APPS += (
    'django.contrib.admin',
    'back',
)
