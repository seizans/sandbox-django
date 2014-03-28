# coding=utf8
from django.shortcuts import render


def hello(request):
    d = {'back_hello_string': 'HELLO BACK APPLICATION'}
    return render(request, 'back/hello.html', d)
