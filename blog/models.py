from django.db import models
from django.contrib.auth import get_user_model


class Tag(models.Model):
    slug = models.CharField(primary_key=True, unique=True, max_length=20)
    name = models.CharField(unique=True, max_length=20)

    def __str__(self):
        return self.slug


class Article(models.Model):
    title = models.CharField(default="", max_length=30)
    text = models.TextField(default="",)
    author = models.CharField(default="", max_length=30)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    count = models.IntegerField(default=0,)
    tags = models.ManyToManyField(Tag, blank=True)  # ManyToMany: 多 対 多,　上記の Tag class 参照、 blank= 空白でもOK


class Comment(models.Model):
    comment = models.TextField(default="", max_length=500)  # 長文の場合
    created_at = models.DateField(auto_now_add=True)  # 作成日時を登録してくれる
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)  # 1 対 多
    article = models.ForeignKey(Article, on_delete=models.CASCADE)  # 1 対 多 : comment は複数有り得る
