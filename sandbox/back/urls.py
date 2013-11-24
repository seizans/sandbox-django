# coding=utf8
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'back.views',
    url(r'^hello$', 'hello'),
)
