from django.conf.urls import patterns, url

urlpatterns = patterns(
    'app1.views',
    url(r'^hello$', 'hello'),
)
