# coding=utf8
# backアプリケーション(管理用)に共通の設定
from .base import *  # NOQA

SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # 管理アプリではブラウザ閉じるとセッション期限切れにする

INSTALLED_APPS += (
    'back',
)
