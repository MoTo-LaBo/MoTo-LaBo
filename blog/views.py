from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article


def article(request):
    objs = Article.objects.all()
    context = {
        'articles': objs,
    }
    return render(request, 'blog/article.html', context)


def article(request, pk):
    obj = Article.objects.get(pk=pk)
    context = {
        'article': obj,
    }
    return render(request, 'blog/article_detail.html', context)
