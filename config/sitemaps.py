from mysite.views import identity, about
from django.contrib import sitemaps
from django.urls import reverse
from blog.models import Article


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5  # 優先度
    changefreq = 'dayily'  # 更新頻度・変更頻度

    def items(self):
        return['mysite:index', 'mysite:identity', 'mysite:about']  # mysite: -> mysite app から読み込むという意味

    def location(self, item):  # url
        return reverse(item)  # item url を返していく


class BlogSitemap(sitemaps.Sitemap):
    priority = 0.5  # 優先度
    changefreq = 'dayily'  # 更新頻度・変更頻度

    def items(self):
        return Article.objects.all()  # 作成した記事全てを sitemap にあげる

    def lastmod(self, obj):  # 作成日の日付が sitemap に記載される。最終更新日にしたい場合は、updated_at(models.py 確認)
        return obj.created_at

    def location(self, obj):  # blog/urls.py name article の情報を取得,pk に対しては object id を渡す
        return reverse('blog:article', kwargs={'pk': obj.id})  # 各記事が特定できるので url path が生成できる
