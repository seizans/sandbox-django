from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^store/', include('store.urls')),
    url(r'^back/', include('back.urls')),
    # Examples:
    # url(r'^$', 'sandbox.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
