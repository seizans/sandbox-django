from django.conf.urls import include, patterns, url
from rest_framework import viewsets, routers

from core.models import Note


class NoteViewSet(viewsets.ModelViewSet):
    model = Note

router = routers.DefaultRouter()
router.register(r'notes', NoteViewSet)

urlpatterns = patterns(
    'api.views',
    # url('^notes$', 'notes'),
    # url('^notes2$', 'notes2'),

    url('^rest/', include(router.urls)),
    url('^auth/', include('rest_framework.urls', namespace='rest_framework')),
)
