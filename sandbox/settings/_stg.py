# coding=utf8
# ステージング用の環境で共通の設定
# base系の後で import * されるので、上書きをする挙動になる

ALLOWED_HOSTS = ['ステージング環境で使うホスト名を入れる']
SECRET_KEY = 'n+i_fly3y8v%(hgp#n(9h3@brw6qjiae)$gauqd)mee1t3dp1u'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dbname',
        'USER': 'dbuser',
        'PASSWORD': 'password',
        'HOST': 'hostname',
        'PORT': '',
    }
}
