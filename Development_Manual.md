# Django Web Practical App ~ GAE -> Deploy

1. Python Django を用いて web app 開発
   - 実用性に重きを置く事が前提
2. Material Design Bootstrap を用いた Design
3. GAE(google app engine), Google Cloud Storage, GitHub を用いて service を公開
## 1. 環境構築と初期設定
- 仮想環境とdjango install と upgrade
### 1. 仮想環境構築
    python3 -m venv venv
### 2. 仮想環境を立ち上げる
    source venv/bin/activate
### 3. django install
    pip install django
### 4. django upgrade
    pip install --upgrade pip
### 5. プロジェクト名
    django-admin startproject < directory名 > .
- directory 名はその時によって変更
- . (ドット)をつけることにより、今いる directory の中に project dir を作成できる
- . がない場合は directory を１つ作成してその中に project dir が作成される
### 6. プロジェクト directory に降りて下記のコマンド実行
    python manage.py runserver
- Starting development server at http://127.0.0.1:8000/
- server が立ち上がっている事を確認
### 7. runserver (127.0.0.1.:8000)
    localhost:127.0.0.1.:8000
- brawer にアクセスする
- localhost = 127.0.0.1.:8000 = 自分の PC brawser
- 8000 = ポート
- Quit the server with CONTROL-C
  - CONTROL-Cでサーバーを終了する
### 8. App 作成
    python manage.py startapp < app名 >
## 2. setting file
### 0. settings.py に import os を追加
    import os
    from pathlib import Path
### 1. settings.py に app を作成した事を記述する
- INSTALLED_APPS に 'mysite', を記述
- ALLOWED_HOSTS = ['*'] どんな host でも許可
  - 本番環境は自身や特定の domain を記述して access domain を限定
- LANGUAGE_CODE = 'ja'
- TIME_ZONE = 'Asia/Tokyo'
### 2. project urls.py file に path 追加
    from django.urls import path, include
    from mysite import views

    path('', views.index),　
- include method も import する
-  ' ' のなかに入ったものは、いかなる場合でも mysite の vews.index を呼び出す
### 2-1. mysite views.py file に記述
    from django.http import HttpResponse


    def index(request):
        return HttpResponse('hello MoTo LaBo site')
### 2-2. localhost で確認
    python manage.py runserver
- hello MoTo LaBo site が表示されれば OK!
### 3. project dir 直下に templates dir 作成
- その中にまた mysite dir を作成する
#### 3-1. templates directory とは？
- views.py で render で返す時に、templates/mysite で作成した HTML file を読みっとて、その情報を response する
#### 3-2. settings.py 記述
    os.path.join(BASE_DIR, 'templates'),
- TEMPLATES = [ ] の 'DIRS':[ ここに記述 ]
- project までの path + templates までの path を通す
- templates / mysite / html file 作成
#### 3-3. views.py 書き換え
    def index(request):
        return render(request, 'mysite/index.html', {})
- 上記で templates までの path を記述したので、引数にはそれ以下の path を記述する
#### 3-4. views.py 書き換え
    def index(request):
        context = {
            'title': 'MoTo LaBo'
        }
        return render(request, 'mysite/index.html', context)
#### context を引数に入れることで html file で使用できるようになる
    <h1>{{ title }}</h1>
- browser では MoTo LaBo と h1 の装飾で表示される
### 4. base.html
- head, footer, menubar etc... 使い回しができる部分は一つの file にまとめてしまう
#### 4-1. 他の html file の一番上に下記を記述する
    {% extends 'mysite/base.html' %}
- template tag {% %}, {{ }} を使用する
- これでどの file でも base.html で記述・設定したものが継承される
#### 4-2. base.html で block conten を記述
    {% block content %}
    {% endblock %}
-  上記を記述する事で index.html やその他 html とbase.html の連携が取れるようになる
#### 4-3. index.html file block conten で囲み記述
    {% extends 'mysite/base.html' %}
    {% block content %}
    <h1>{{ title }}</h1>
    <p>hello MoTo LaBo site</p>
    {% endblock %}
- browser では、base.html の継承と index.html の記述したものが表示される

### 5. livereload
> https://pypi.org/project/django-livereload-server/
- 自動でリロードしてくれる
- settings.py に記述
  - INSTALLED_APPS [　] の
    - 'django.contrib.staticfiles'の前に記述
    - ドキュメントに記述してある
  - MIDDLEWARE [ ] に
    - 'livereload.middleware.LiveReloadScript',
#### 5-1. livereloadサーバーを起動
    python manage.py livereload
- livereload server は起動したままにする
- error がでた場合は port 番号を変えないといけない
  - ドキュメントに記載してある
#### 5-2. terminal を１つ追加して
    python manage.py runserver
- localserver も起動させておく
#### 5-3. 常時２つが起動している状態
- これで file 編集後 -> save -> 自動 reload してくれる
- **save した段階で自動で Reload してくれる**
### 5-4. MDB(Material Design Bootstrap)
- CDN の CSS と JS を base.html に読み込み
> https://mdbootstrap.com/docs/standard/getting-started/installation/
### 5-5. static direcotry 作成
    STATICFILES_DIRS = [
        os.psth.join(BASE_DIR, 'static'),
    ]
- root 直下に static dir 作成
  - その中に scss, css, img, js etc...
- settings.py に上記を記述 path を通す
### 5-6. base.html に下記を記述
    <!DOCTYPE html>
    {% load static %}
    <html lang="ja">
- load static tag を 全ての html file 上記に記述する
### 5-7. include template tag
    {% include 'mysite/snippets/header.html' %}
1. snippets dir 作成 -> base.html から header.html, footer.html を作成
2. snippets dir に入れる
3. base.html に include template tag 1行を記述する事でかなりスッキリする
## 6. blog app 作成
    python manage.py startapp blog
### 6-1. config dir settings.py に記述
  - INSTALLED_APPS [　] の
    - 'blog', を記述
- config dir urls.py に paht を記述
  - path('blog/', include('blog.urls')),
  - blog/ : blog という url が選択された時は、blog/ 以下の blob.url に飛ばす
### 6-2. blog dir に urls.py 作成
    urlpatterns = [
        path('test/', views.test),
    ]
- urls.py に blog/ 以降の path を記述する
  - views.test を参照
### 6-3. views.py に関数を記述
    from django.shortcuts import render
    from django.http import HttpResponse


    def test(request):
        return HttpResponse('test page')

    # localserver
- views.py に 上記を記述して、localserver で表示できるか確認
> http://127.0.0.1:8000/blog/test/
- test page が表示されれば OK
### 6-4. blog dir models.py
    class Article(models.Model):
        title = models.CharField(default="", max_length=30)
        text = models.TextField(default="",)
        author = models.CharField(default="", max_length=30)
        create_at = models.DateField(auto_now_add=True)
     updated_at = models.DateField(auto_now=True)
- class 作成（db.sqlite3 table 作成）
  - title 以下は全て列名
  - max-length は文字数指定
  - auto_now_add は data が新規作成されたその時だけの日時を入力してくれる
  - auto_now は data が更新される度に日時を更新してくれる
  - default は data が作成された時の初期値
    - null(何もない)を使用したくないので設定する
    - 何もない時は空白(文字列)ですよという指示
    - blank=True : 空白のままでok. default は False
    - null=True : null の値を入れる事ができる. default は False
## 7. 管理画面の登録(user model 作成)
- 管理画面に入るには user 登録が必要になる
- django には標準で user model が搭載されている
  - user name と password で login できるが柔軟性がない
- 一般の site だと email や password で login できる事が多い
  - django 標準のだと初期の変更や、その他の応用的な対応ができないので、カスタム user を作成していく
### 7-1. mysite models.py に下記を記述
### 7-2. カスタム User model AbstractBaseUser(アブストラクトベースユーザー)
- User model の中で一番柔軟性が高い
  - email を使用して login
    - 文字数指定、email 重複無し
    - 一般 user と admin user check, 権限付与
#### **詳しくは mysite dir models.py 参照**
### 7-3. setting.py 記述
    AUTH_USER_MODEL = 'mysite.User'
- django では標準の user model があるが今回は、作成した User model を使用の指示
- 7-2 で作成した model
### 7-4. mysite dir admin.py(管理画面の表示設定)
- 通常の model の場合は簡単にできる
- 今回はカスタム model を作成しているので、使用に必要な記載がある
#### **詳しくは mysite dir admin.py 参照**
### 7-5. makemigrations -> migrate
    # 1. migrations に file 作成
    python manage.py makemigrations

    # 2. db に適用(反映)させる
    python manage.py migrate
- table 作成
- 0001 -> migrations -> 0002(0001との差分)
  - 作成 file を辿っていけば、差分を確認できる
### 7-6. 管理画面 login
    python manage.py createsuperuser
1. superuser (なんでもできる全権限をもったuser)を作成する必要がある
2. email, password を登録
3. > http://127.0.0.1:8000/admin/
4. email, password 入力 login
### 7-7. blog dir admin.py
- admin に Article 反映
  - 管理画面（admin）記事作成
## 8. 記事の表示・反映
- template tag を使用して for文で記述
### 8-1. blog app views.py
    def articles(request):
        objs = Article.objects.all()
        context = {
            'articles': objs,
        }
        return render(request, 'blog/article.html', context)
1. all() で models.py で定義した tabel column を全て取得
2. objs に入れて、articales という name で使用
### 8-2. article.html に template tag で記述
    {% for obj in articles %}
    {{ obj.title }}
    {{ obj.text }}
    {{ obj.author }}
    {{ obj.create_at }}
    {{ obj.id }}
    {% endfor %}
1. for 文で回して、admin で作成した記事の情報を入れていく
2. aricles は obj という変数に入れて使用
### 8-3. 記事の puraimari key を取得
    # urls
    path('<slug:pk>/', views.article),

    # views
    def article(request, pk):
        obj = Article.objects.get(pk=pk)
        context = {
            'article': obj,
        }
        return render(request, 'blog/article_detail.html', context)
1. get(pk=pk) で pk 取得
2. obj に格納 article という name で使用
3. urls.py に path 追記
4. article.html に link tag < a href="/blog/{{ obj.id }}/" > tag を作成して、各記事の詳細に飛ばす
5. article_detail.html 記事詳細作成
### 8-4. pagenation 実装
    from django.core.paginator import Paginator

    def articles_list(request):
    objs = Article.objects.all()
    paginator = Paginator(objs, 6)
    page_number = request.GET.get('page')
    context = {
        'page_obj': paginator.get_page(page_number),
        'page_number': page_number,
    }
1. django の paginator class 使用
2. paginator = object の塊を渡している:(objs, 6)
   - 1 page に表示する数を指定:(6記事表示)
3. **GETの意味**
   - paginator によって自動で page ulr をつけてくれて、表示する記事の数を制限している
     - http GET
     - http://example.com/kiji/?page=1&id=123
     - page=1 -> key = value の関係
     - & をつけると繋げる事ができる
4. context の 'articles': objs, は削除して page_obj　だけにしている
   - **article_list.html の for文書き換え**
   - {% for obj in articles %} -> {% for obj in page_obj %} に変更
## 9. 認証機能実装
    # urls.py
    path('login', views.login),

    # views.py
    def login(request):
    context = {}
    return render(request, 'mysite/login.html', context)

1. config dir urls.py に上記を記載
2. mysite app(dir) views.py に login に必要な関数を記述
3. template/mysite/login.html と base_auth.html 作成
4. base_auth.html は認証系の base html として作成

