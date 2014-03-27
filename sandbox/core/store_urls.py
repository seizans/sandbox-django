from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^store/', include('store.urls')),
    url(r'^search/', include('haystack.urls')),
    url(r'^api/', include('api.urls')),
)
