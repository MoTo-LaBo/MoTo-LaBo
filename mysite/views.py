from django.contrib.auth import forms
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from blog.models import Article
from mysite.forms import UserCreationForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.core.mail import send_mail
import os


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
            # login させる (from django.contrib.auth import login)
            login(request, user)

            messages.success(request, 'Registration Complete')
            return redirect('/')
    return render(request, 'mysite/auth.html', context)


@login_required  # 関数用(mypage に access するには login していないと access できない/.decorators import login_required)
def mypage(request):
    context = {}
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Account Update Complete')
    return render(request, 'mysite/account.html', context)


def contact(request):
    context = {}
    if request.method == 'POST':

        # ------- email -------
        subject = 'お問合せがありました'
        message = "お問合せがありました。\n名前: {}\nメールアドレス: {}\n内容: {}".format(
            request.POST.get('name'),
            request.POST.get('email'),
            request.POST.get('content'))

        email_from = os.environ['DEFAULT_EMAIL_FROM']
        email_to = [os.environ['DEFAULT_EMAIL_FROM'], ]
        send_mail(
            subject,
            message,
            email_from,
            email_to
        )
        # ------- email -------
        messages.success(request, 'お問い合わせ頂きありがとうございます')
    return render(request, 'mysite/contact.html', context)
