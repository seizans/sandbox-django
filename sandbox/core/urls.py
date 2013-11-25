from django.conf import settings
from django.conf.urls import patterns, include, url

if settings.IS_FRONT:
    urlpatterns = patterns(
        '',
        url(r'^store/', include('store.urls')),
    )
else:
    from django.contrib import admin
    admin.autodiscover()
    urlpatterns = patterns(
        '',
        url(r'^back/', include('back.urls')),
        url(r'^admin/', include(admin.site.urls)),
    )
