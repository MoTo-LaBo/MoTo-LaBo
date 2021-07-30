from django.core import paginator
from django.shortcuts import render
from blog.models import Article, Comment
from django.core.paginator import Paginator
from blog.forms import CommentForm


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
    if request.method == 'POST':
        form = CommentForm(request.POST)  # バリデーションもしてくれるので form 使用
        # print(form)   terminal comment の内容を表示してくれる
        if form.is_valid():  # error がないか確認
            comment = form.save(commit=False)
            comment.user = request.user
            comment.article = obj
            comment.save()
        # comment = request.POST.get('comment')
        # context['test'] = comment
    comments = Comment.objects.filter(article=obj)
    context = {
        'article': obj,
        'comments': comments
    }
    return render(request, 'blog/article_detail.html', context)
