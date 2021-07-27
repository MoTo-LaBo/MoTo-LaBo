from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'title': 'MoTo LaBo'
    }
    return render(request, 'mysite/index.html', context)


def login(request):
    context = {
    }
    return render(request, 'mysite/login.html', context)
