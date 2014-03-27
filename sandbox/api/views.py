# coding=utf8

from django.http import JsonResponse


def notes(request):
    content = {
        'hoge': 'fuga',
        'mado': [1, 3, 5],
    }
    return JsonResponse(content)

from django.http import HttpResponse
import simplejson as json


def notes2(request):
    content = {
        'hoge': 'fuga',
        'mado': [1, 3, 5],
    }
    body = json.dumps(content)
    return HttpResponse(body, content_type='application/json')
