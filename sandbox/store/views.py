# coding=utf8
from django.shortcuts import render

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
