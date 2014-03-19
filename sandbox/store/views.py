# coding=utf8

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import CreateView
from haystack.query import SearchQuerySet

from core.models import Note
from core.search_indexes import NoteIndex


def hello(request):
    d = {'from_hello_view': 'From Hello View'}
    return render(request, 'store/hello.html', d)


def insert_note(request):
    note1 = Note.objects.create(title=u'タイトル', author=u'著者', content=u'内容')
    NoteIndex().update_object(note1)
    note2 = Note.objects.create(title='title1', author='author1', content='content1')
    NoteIndex().update_object(note2)
    d = {'from_hello_view': 'From Hello View'}
    return render(request, 'store/hello.html', d)


class NoteView(CreateView):
    model = Note
    template_name = 'store/note.html'
    success_url = reverse_lazy('note')

    def get_context_data(self, **kwargs):
        context = super(NoteView, self).get_context_data(**kwargs)
        context['notes'] = Note.objects.all()
        context['query'] = SearchQuerySet().models(Note).filter(title=u'定食')
        return context
note = NoteView.as_view()
