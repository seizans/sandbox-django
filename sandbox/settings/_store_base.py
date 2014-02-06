# coding=utf8
# storeアプリケーション(表側)に共通の設定
from ._base import *  # NOQA

ROOT_URLCONF = 'core.store_urls'

SESSION_COOKIE_AGE = 60 * 60 * 24 * 30  # 30日間

INSTALLED_APPS += (
    'store',
)
