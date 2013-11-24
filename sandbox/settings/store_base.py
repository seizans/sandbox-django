# coding=utf8
# storeアプリケーション(表側)に共通の設定
from .base import *  # NOQA

SESSION_COOKIE_AGE = 60 * 60 * 24 * 30  # 30日間
