from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article


def article(request):
    objs = Article.objects.all()
    context = {
        'title': 'MoTo LaBo',
        'articles': objs,
    }
    return render(request, 'blog/article.html', context)
