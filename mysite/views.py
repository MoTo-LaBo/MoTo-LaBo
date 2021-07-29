from django.contrib.auth import forms
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from blog.models import Article
from mysite.forms import UserCreationForm
from django.contrib import messages


def index(request):
    context = {
        'title': 'MoTo LaBo'
    }
    return render(request, 'mysite/index.html', context)


class Login(LoginView):
    template_name = 'mysite/auth.html'

    def form_valid(self, form):
        messages.success(self.request, 'Logging in')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error')
        return super().form_invalid(form)


def signup(request):
    context = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # user.is_active = False
            user.save()
            messages.success(request, 'Registration complete')
            return redirect('/')
    return render(request, 'mysite/auth.html', context)
