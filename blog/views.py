from django.core import paginator
from django.shortcuts import render
from blog.models import Article
from django.core.paginator import Paginator


def articles_list(request):
    objs = Article.objects.all()
    paginator = Paginator(objs, 6)
    page_number = request.GET.get('page')
    context = {
        'page_obj': paginator.get_page(page_number),
        'page_number': page_number,
    }
    return render(request, 'blog/article_list.html', context)


def article(request, pk):
    obj = Article.objects.get(pk=pk)
    context = {
        'article': obj,
    }
    return render(request, 'blog/article_detail.html', context)
