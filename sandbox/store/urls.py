from django.conf.urls import patterns, url

urlpatterns = patterns(
    'store.views',
    url(r'^hello$', 'hello'),
)