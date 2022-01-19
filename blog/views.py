from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core import paginator
from django.shortcuts import render
from blog.models import Article, Comment, Tag
from django.core.paginator import Paginator
from blog.forms import CommentForm


def articles_list(request):
    objs = Article.objects.all().order_by("-created_at")  # .order_by 作成日が新しい順
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
        if request.POST.get('like_count', None):  # いいね追加
            obj.count += 1
            obj.save()
        else:
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


def tags(request, slug):
    tag = Tag.objects.get(slug=slug)
    objs = tag.article_set.all()  # 逆参照: tag を参照している Article を全て取得する

    paginator = Paginator(objs, 6)
    page_number = request.GET.get('page')
    context = {
        'page_obj': paginator.get_page(page_number),
        'page_number': page_number,
    }
    return render(request, 'blog/article_list.html', context)


@ensure_csrf_cookie
def like(request, pk):
    d = {'message': 'error'}
    if request.method == 'POST':
        obj = Article.objects.get(pk=pk)
        obj.count += 1
        obj.save()

        d['message'] = 'success'
    return JsonResponse(d)
