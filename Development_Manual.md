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
