from django.contrib.auth import forms
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from blog.models import Article
from mysite.forms import UserCreationForm


def index(request):
    context = {
        'title': 'MoTo LaBo'
    }
    return render(request, 'mysite/index.html', context)


class Login(LoginView):
    template_name = 'mysite/auth.html'


def signup(request):
    context = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # user.is_active = False
            user.save()
    return render(request, 'mysite/auth.html', context)
