from django.conf.urls import patterns, url

urlpatterns = patterns(
    'api.views',
    url('^notes$', 'notes'),
    url('^notes2$', 'notes2'),
)
