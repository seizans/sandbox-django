# coding=utf8
# 管理用アプリケーションの、開発環境用の設定
from ._back_base import *  # NOQA
from ._dev import *  # NOQA

# .dev で定義されている追加分を追加する
INSTALLED_APPS += INSTALLED_APPS_PLUS
MIDDLEWARE_CLASSES += MIDDLEWARE_CLASSES_PLUS
