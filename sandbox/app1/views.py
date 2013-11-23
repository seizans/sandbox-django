from django.shortcuts import render


def hello(request):
    d = {'from_hello_view': 'From Hello View'}
    return render(request, 'app1/hello.html', d)
