# Django Web Practical App ~ GAE -> Deploy

1. Python Django を用いて web app 開発
   - 実用性に重きを置く事が前提
2. Material Design Bootstrap を用いた Design
3. GAE(google app engine), Google Cloud Storage, GitHub を用いて service を公開
## 1. 環境構築と初期設定
- 仮想環境とdjango install と upgrade
#### 1-1. 仮想環境構築
    python3 -m venv venv
#### 1-2. 仮想環境を立ち上げる
    source venv/bin/activate
#### 1-3. django install
    pip install django
#### 1-4. django upgrade
    pip install --upgrade pip
#### 1-5. プロジェクト名
    django-admin startproject < directory名 > .
- directory 名はその時によって変更
- . (ドット)をつけることにより、今いる directory の中に project dir を作成できる
- . がない場合は directory を１つ作成してその中に project dir が作成される
#### 1-6. プロジェクト directory に降りて下記のコマンド実行
    python manage.py runserver
- Starting development server at http://127.0.0.1:8000/
- server が立ち上がっている事を確認
#### 1-7. runserver (127.0.0.1.:8000)
    localhost:127.0.0.1.:8000
- brawer にアクセスする
- localhost = 127.0.0.1.:8000 = 自分の PC brawser
- 8000 = ポート
- Quit the server with CONTROL-C
  - CONTROL-Cでサーバーを終了する
#### 1-8. App 作成
    python manage.py startapp < app名 >
## 2. setting file
#### 2-0. settings.py に import os を追加
    import os
    from pathlib import Path
### 2-1. settings.py に app を作成した事を記述する
- INSTALLED_APPS に 'mysite', を記述
- ALLOWED_HOSTS = ['*'] どんな host でも許可
  - 本番環境は自身や特定の domain を記述して access domain を限定
- LANGUAGE_CODE = 'ja'
- TIME_ZONE = 'Asia/Tokyo'
#### 2-2. project urls.py file に path 追加
    from django.urls import path, include
    from mysite import views

    path('', views.index),　
- include method も import する
-  ' ' のなかに入ったものは、いかなる場合でも mysite の vews.index を呼び出す
#### 2-3. mysite views.py file に記述
    from django.http import HttpResponse


    def index(request):
        return HttpResponse('hello MoTo LaBo site')
#### 2-4. localhost で確認
    python manage.py runserver
- hello MoTo LaBo site が表示されれば OK!
## 3. project dir 直下に templates dir 作成
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
## 4. base.html
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

## 5. livereload
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
> https://pypi.org/project/django-livereload-server/
- error -> Error: That port is already in use.
  - port 番号の変更
#### settings.py に下記を記述
    LIVERELOAD_PORT = '8080'
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
5. {% include 'mysite/login.html' %} template tage で base_auth.html 記述
### 9-1. POST 送信 : mysite app(dir)
    # login.html
    <form class="login_form" method="POST" action="">
    {% csrf_token %}
    {{ req }}

    # views.py
    def login(request):
        context = {
        }
        if request.method == 'POST':
            context['req'] = request.POST
        return render(request, 'mysite/login.html', context)

1. POST -> 送信　action -> 送信先を指定する事もできる
2. **{% csrf_token %}** は, form には必須！！
3. views.py に login 関数を記述で　login の値が帰ってきているかを test する
4. {{ req }} に入力した password, email が表示される
### input tag
- input tag の name = username に変える
  - name = email だと django の標準をそのまま上書きしてしまい挙動がおかしくなる
### 9-2. LoginView template tag (if)
    # config/ urls.py
    path('login', views.Login.as_view()),

    # views.py
    from django.contrib.auth.views import LoginView

    class Login(LoginView):
    template_name = 'mysite/login.html'

1. 直接 'login' -> views.Login.as_view('template/〇〇.html')
    - 上記のように urls.py に記載すれば、views.py に記述する手間が省ける
    - login に入ったら、そのまま ('template/〇〇.html') に飛ばしてくれる
    - 今回は他の追加項目もあるので views.py で class Login を作成
### 9-3. login.html で login 確認
        {% if request.user.is_authenticated %}
        ログイン中
        {% else %}
        ログインしていません
        {% endif %}
- user -> django が標準で搭載している user 認証機能
- True or False で login の有無を確認
- bjango には便利な tenplate tag が気軽に使える
### 9-4. config / settings.py
    LOGIN_URL = '/login/'

    LOGIN_REDIRECT_URL = '/login/'
1. login する url を指示
2. login 後に飛ばす url を指示
### 9-5. logout 機能実装
    # config dir

    # urls.py
    from django.contrib.auth.views import LogoutView

    path('logout/', LogoutView.as_view()),

    # setting.py
    LOGOUT_URL = '/logout/'

    LOGOUT_REDIRECT_URL = '/login/'

1. urls.py に上記を記載
2. settings.py 上記を記載
3. login.logout できるか確認
4. ログイン中と表示されれば成功
## 10. 新規登録の機能実装
    # config dir

    # urls.py
    path('signup/', views.signup),
1. urls.py に上記を記載
2. mysit app に forms.py file 作成
   - バリデーション(検証する機能)、passwordをハッシュ化(打った文字を判断出来ないよう形で保存)
   - forms.py 参照
### 10-1. mysite app views.py
    from mysite.forms import UserCreationForm

    def signup(request):
        context = {}
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                # user.is_active = False
                user.save()
        return render(request, 'mysite/auth.html', context)
1. views.py に上記を記載
2. POST で入力された data を creation forms.py に回す
   - 今回はバリデーション、 passwordハッシュ化
3. error がなければ userの情報を元に新規作成する
#### 4. commit = False
    user = form.save(commit=False)
- save は仮に user object を作成している感じ
  - まだ data base には保存していない
- なのでここで次のような追加の項目を入れる事もできる
#### 5. is_active = False
    user.is_active = False
- mysite app models.py で定義してあるモノがあれば使用できる
#### models.py 参照
    # アカウントが有効かどうかの判断。user 登録が完了したら有効なので、True
    is_active = models.BooleanField(default=True)

    # 管理画面に入れるかどうか。管理者かどうか。一般 user が入れてはいけないので、 False
    is_admin = models.BooleanField(default=False)
#### default が True なので…
    user.is_active = False
- あえて False にして、送信はされたが…
- まずは検証をする。折り返しの mail を返し、Link がクリックされると初めて検証が OK!
- OK になったら active = True にする
- という事もできる
### 10-2. auth.html
    {% if 'login' in request.path %}
    Login
    {% elif 'signup' in request.path %}
    新規登録
    {% endif %}
- auth.html に上記を記載
  - 今回は login も 新規登録も HTML の中身がほとんど変わらないので HTML file を１つにする為に **URL** で切り替えて表示する
  - 同じような file を２つ作る必要性は無い為。TPOによって変える
#### path によって変わるか確認
    {{ request.path }}
- 上記を一緒に記載して確認してみる
- path が変わると一緒に path と文字が変わる
  - http://127.0.0.1:8000/signup/
    - /signup/ 新規登録
  - http://127.0.0.1:8000/login/
    - /login/ Login
#### input tag name 属性の中にも追加
    name="{% if 'login' in request.path %}username{% elif 'signup' in request.path %}email{% endif %}
- 上記と同じ事をしている
  - もし path に login が含まれていたら name 属性を username にする
  - もし path に signup が含まれていたら name 属性を email にする
- browser の検証 Tool で確認
### 実際に新規登録してみる
- 新規登録画面でとろくしてみる
- admin 画面で確認
- 新規 user で login してみる
## error 発生
    # auth.htm
    <p>
        request.userは {{ request.user }}
        <br>
        request.user.is_authenticatedは　{{ request.user.is_authenticated }}
    </p>
- 上記を追記して確認をしてみる
### 結果
    request.userは AnonymousUser
    request.user.is_authenticatedは　False

    request.userは匿名ユーザー
    request.user.is_authenticatedはFalseです
- 実際にログイン自体ができていないためにログインページに飛ばされている
### 解決
    # error code
    <input type="email" id="id_email" class="form-control" placeholder="Email address" name="{% if 'login' in request.path %}username{% elif 'signup' in request.path %}email{% endif %}" required autofocus>

    # After correction
    <input type="email" id="id_email" name="{% if 'login' in request.path %}username{% elif 'signup' in request.path %}email{% endif %}" class="form-control" placeholder="Email address" required autofocus>
- 原因は…　**name 属性の位置で error が出ていた**
  - タイポや空白だけではなく、属性の位置(前後)が違うだけでも error が出る！！
  - 初めてだったので、今後はその事も頭に入れて error 解決を探る
### 10-3. 新規登録機能の Final touches
    # mysite views.py
    from django.contrib import messages

    # 関数 signup に追記
    messages.success(request, 'Registration complete')
    return redirect('/')
1. Registration complete = 登録完了
2. 登録完了後は top (index.html) へ飛ばす
3. settings.py に下記を作成 (settings.py 参照)
   - massage tab with bootstrap alert class
4. mysite/snippets/ messages.html 作成
5. base.html に include
   - {% include 'mysite/snippets/messages.html' %}
6. User 新規作成 top に飛ばされて Alert が表示されれば実装完了！
#### django 版コメントアウト
    {% comment %} ここに記述されたものはコメントアウトされる {% endcomment %}
- html, css, scss, 色々なコメントアウトがあるが上記の django 版の場合は検証 Tool にも表示されない
- Browser の検証でも見られたく無いものは django 版のコメントアウトを使用
> python はバックエンドで事前に template(html) を render(生成) するので、その時にコメントアウトのところは削除される
### 10-4. login も同じように実装
    # class Login に追記

    def form_valid(self, form):
        messages.success(self.request, 'Logging in')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error')
        return super().form_invalid(form)
1. login 出来た場合の message 関数
2. login 出来なかった場合の message 関数
### 10-5. message.html
    {% for msg in messages %}
    <div class="alert alert-light fade show {{ msg.tags }}" role="alert" data-mdb-color="secondary">
        <i class="fas fa-sign-in-alt"></i>
        {{ msg }}
    </div>
    {% endfor %}
- template tag を使用。messages を msg で for文で回して表示させる
-  {{ msg }} -> 上記の view で定義した文字が表示される
-  {{ msg.tags }} -> settings.py で作成した class が記載される
### 10-6. paht による切り替え
    {% if 'login' in request.path %}
    <div class="test-center">
        <a href="/signup/" class="link-secondary">新規登録へ</a>
    </div>
    {% elif 'signup' in request.path %}
    <div class="text-center">
        <a href="/login/" class="link-secondary">Loginへ</a>
    </div>
    {% endif %}
1. login, signup の path によって飛ばす場所を変える
2. 新規登録とログインへ飛ばす link を記述
### 10-7. user が login しているか、いないかで切り替え
    {% if user.is_authenticated %}
    <li class="login_out"><a href="/logout/" class="bg_black">Logout</a></li>
    {% else %}
    <li class="login_out"><a href="/login/" class="bg_black">Login</a></li>
    <li class="author"><a href="/signup/">Create User</a></li>
    {% endif %}
1. ここでは path の認証が使用できないので、user が認証されているなら(login しているかどうか)で切り替え
   - authenticated True or False で切り替え
2. login していれば logout button を表示
3. logout していれば login button と 新規作成 button を表示
## 11. コメント欄作成
    comment.html 参照
1. mysite/snippets/ comment.html 作成
2. article_detail.html に comment.html を　include する
   - {% include 'mysite/snippets/comment.html' %}
3. if 文で login している時としていない時の切り替えをする
4. {% if user.is_authenticated %}を使用
### 11-1. model 作成
    # blog/ models.py
    from django.contrib.auth import get_user_model

    class Comment(models.Model):
    comment = models.TextField(default="", max_length=500)
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
1. 長文の場合は TextField
2. DataFild(auto_now_add=True) 作成日時の登録
## 11-2. **ForeignKey()**
> comment に対してどの user が書いたのか？ usename, id, email を保持
- ここに user の名前は入れない！！！
  - もし comment した user が name を変更した場合、すでに変更前で記載している情報をわざわざ過去に戻って全て更新しないといけなくなる
  - どの user が記述したのか分からなくなる
  - わかっても、過去の use name を全て 新しい user name に更新する事になる
#### **「そこで登場するのが ForeignKey 」**
- **ForeignKey** に対するのが **PrimaryKey(pk)**
  - **PrimaryKey**
    - それぞれの table には id があって、絶対に同じにならないようになっている。それで初めてどのレコードかを参照できる
  - **ForeignKey**
    - comment からみて user を参照する
    - comment -> user pk(primarykey) をみる
    - 外部から参照している = ForeignKey
- user name を直接書いていい場合もある。履歴を変更しないなど…
- 変更しても大丈夫で、過去の user name の記録を取っておきたい場合も記述しても大丈夫
- **記述のメリット・デメリットを考えて使用する事**
#### 「多くの場合は変更が必要なので ForeignKey を使用する」
- <u>**ForeignKey = 1 対 多**</u>
  - 一人の user は複数の comment を投稿する可能性が有り得る
  - comment を記述したのはその人自身(1人)でしか有りえない
  - １つの comment に対して複数 user が書いているという事は有りえない
  - 上記の理由から **ForeignKey** を使用する
### on_delete=models.CASCADE
  - ForeignKey には必須な記述項目
  - user や記事が削除された時に comment はどうしますか？その場合の対処の仕方
  - 今回は **CASCADE** -> <u>その user が削除された場合は comment も一緒に削除する</u>
  - article のも同じく、記事が削除されたら一緒に comment も削除する
### ForeignKey, One To One, Many To Many
- django class 参照の仕方
- comment と user の相互の参照関係をみた時によって使用するモノを変える
  - <u>**ForeignKey = 1 対 多**</u>
  - <u>**One To One = 1 対 1**</u>
  - <u>**Many To Many = 多 対 多**</u>
### 11-3. makemigrations, migrate
- blog/models.py を database に反映させる
- blog/admin.py file にも記載
  - admin.site.register(Comment)
  - これで管理画面でも表示・閲覧できる
- blog/views.py
  - Comment を関数に記載
- Comment を表示させるために、comment.html 追記・編集
  - list-group の中を template tag を使って for文でまわす
  - views で渡した変数と models に登録した変数を template tag　を使用して回す
  - comment.html 参照 -> < textarea name="comment" > 追記
- blog/ views.py
### error
- form で作成した comment を投稿できなかった
- 投稿された内容が terminal で表示傘れない…
  - タイポや def, class, の間違いではなくform の使い方が hmtl のルールにそっていなかった
  - form の button tag を a tag にしていた事が原因
#### error code (投稿ボタンtag)
    <form method="POST" class="mt-4">
        {% csrf_token %}
        <div class="">
            <label>Post Comment</label>
            <textarea name="comment" class="rounded-0 bg-light form-control　mb-4" rows="1">
            </textarea>
        </div>
        <div class="">
            <button class="btn btn-light me-2" type="submit">Submission</button>
            <!-- <a href="#" class="btn btn-light me-2">Submission</a> --> error の原因
        </div>
    </form>
1. 最初は < a > tag を使用していた。Comment 投稿ができない
2. < button > tag に変えて Comment 投稿ができるようになった
3. type="submit" …… フォーム入力内容を送信するサブミットボタン（初期値）
### 11-4. mysite models.py 編集
- 今後の管理・メンテナンスがしやすいように models dir 作成
  - file を分けて記述していく
  - mysite dir 参照
  - admin 画面に反映させる為に admin.py を編集 (admin.py 参照)
- mypage(profile用 account.html作成)
### 11-5. account 登録内容の反映
- 登録された情報を home に回して、バリデーション -> 保存
1. mysite/ forms.py, views.py に class ProfileForm 追記
2. accuount page で登録してみる -> admin画面で user 情報を確認
3. 今登録されている情報を accuount box に表示
    - accoutn.html の input tag に value="{{ user.profile.〇〇(fieldsで記述したモノ) }}
    - 上記のように追記すれば、現在login user の登録している情報を表示させる事ができる
    - One To One で user と profile が紐づいているので profile model で登録したモノを取得できる
#### fileds
    model = Profile
    fields = (
        'username',
        'zipcode',
        'prefecture',
        'city',
        'address',
    )
## 12. いいね機能実装
- 今回は誰が押しても、いいねのカント数が増えるやり方で実装
1. blog/models.py に追記
####
    # class Article
    count = models.IntegerField(default=0,)

    python manage.py makemigrations
    python manage.py migrate
2. blog/views.py Articleに追記
3. snippets/like_count.html 作成
4. {{ article.count }} template tag　を使用
5. {{ inculde 'mysite/snippets/like_count.html' }} を article_detail.html 記述
### 12-1. 各種 tag 作成
1. blog/models.py 追記編集
2. tag 関数記述 -> article 関数に下記を追記
   - tags = models.ManyToManyField(Tag, blank=True)
3. python manage.py makemigrations
4. python manage.py migrate
5. blog/admin.py, admin 画面で表示・作成できるように追記
#### admin 画面を update
    model = Article.tags.through

    class ArticleAdmin(admin.ModelAdmin):  Article 画面
        inlines = [TagInline]
        exclude = ['tags', ]
- Tag でタグを作成して、 Article 画面でも tag の選択削除ができるように編集
### Many To Many (多 対 多)
- 一つの記事に対して、複数の tag がつく -> 1 対 多
- tag からみた場合も 1つの tag に対して複数の記事で使用されている 1 対 多
  - なので tag は、どちらか見ても、「 多 対 多 」の関係になる
#### 「 多 対 多 」の場合 django では、<u>中間table(sql:batabase)が作成される</u>
- 直接的な関係ではなく、中間に table を挟んでの関係
## 13. お問合せ page 実装
1. contact.html 作成
2. mysite/views.py contact 関数を編集・追記
3. account.html と内容はほとんど同じ
### 13-1. mail 送信先実装
- settings.py は重要な password などは載せない
  - 環境変数を使用して読み込むようにする事
  - file を分けて使用する事
1. project/secrets dir を作成
2. secrets/secret_dev.yaml を作成
#### 3. PyYAML install
    pip install PyYAML

    pip install --upgrade pip
### 4. settings.py に yaml import
    # yaml file
    password: 'パスワードです'

    # settings.py
    import yaml
    with open(os.path.join(BASE_DIR, 'secrets', 'secret_dev.yaml')) as file:
        obj = yaml.safe_load(file)
        os.environ['password'] = obj['password']
        print('-------', os.environ['password'])
- yaml file に password を記述して
- settings.py に yaml file を import する
- 'パスワードです' が使用できる
- os.environ[' password '] は環境変数
### 5. settings.py file に下記を記述
    # --------- Gmail 送信設定 --------------
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
    EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
- os.environ[' EMAIL_HOST_USER ']
- os.environ[' EMAIL_HOST_PASSWORD ']
  - 上記の２つは yaml file に記述
  - あくまで settings.py には環境変数を記述する
## 14. static
    # ----- static 設定項目 -----
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
    ]

    # 〇〇.htm
    {% load static %}
    {% static 'mysite/〇〇.html' %}

1. 上記を settings.py に記述する
2. path を通す
   - BASE_DIR は、project の root directory になっている
3. static file を使用する html に上記の template tag を記述する
   - {% load static %} をする
   - {% static 'mysite/〇〇.html' %} -> static から現在の html までの path
## 15. cloud SDK install
> https://cloud.google.com/sdk/docs/quickstart-macos
### install

    # 1.
    ./google-cloud-sdk/install.sh

    # google に協力するかどうか？
    y or N
    今回は N

    # gcloud command を作成するか？ path を通すか？
    # deploy の時などに gcloud command を treminal で使用するので作成
    Y or n
    Y

    # ~.zshrc file を update するかどうか？
    Enter

    # 2. SDKを初期化
    ./google-cloud-sdk/bin/gcloud init

    # 再起動
    source ~/.zshrc

    # update
    gcloud components update

    # SDKを以前にインストールしたバージョンに戻すには、以下を実行
    gcloud components update --version 349.0.0
### 15-1. GAE deploy 準備
1. project/app.yaml 作成
> https://cloud.google.com/appengine/docs/standard/python3/config/appref
2. deploy に必要な情報を記載
- 今回は github にも app.yaml file をあげれるように、重要な記載は secret/secret_dev.yaml で管理
- 環境変数として app.yaml に読み込む
### 15-2. 必要な library install
    # install
    pip  install gunicorn

    # 使用しているlibrary 書き出し
    pip freeze > requirements.txt
### 15-3. deploy
    # 1. login
    gcloud auth login

    # 2.  project id
    gcloud config set project PROJECT_ID(GCPで作成したproject id)

    # 3. gcloud init で現在の情報を確認
    gcloud init

    # 4. deploy
    gcloud app deploy --project < project id >

    # 5. app を browse で表示する
    gcloud app browse
### 15-4. 細かな修正
1. settings.py で本番環境と開発環境の分岐
2. DEBUG = False, True の使い分け
## 16. DataBase Cloud SQL & MySQL
    OperationalError at /login/
    attempt to write a readonly database
- login すると上記の error が出る
  - **原因** -> SQLite3 を使用しているから
  - SQLite3は気軽に使用できるのだが、簡単にdata削除できてしまう
### 16-1. cloud SQL
> https://cloud.google.com/python/django/appengine
### code
    # API の認証情報を取得して認証
    gcloud auth application-default login

    # Cloud SQL Auth Proxy をダウンロード
    curl -o cloud_sql_proxy https://dl.google.com/cloudsql/cloud_sql_proxy.darwin.amd64

    # Cloud SQL Auth Proxy を動作可能にする
    chmod +x cloud_sql_proxy
### 16-2. db の反映
- settings.py file を編集
  - 今回は secret.yaml を作成しているので、settings.py には環境変数を使用して github にあげても大丈夫なようにする
  - <u>間違っても secrets dir は上げないこと</u>
### 16-3. MySQL install
    # 1.
    brew install mysql

    # 2. django 推奨 (MySQL を使用する時は必要になる library)
    pip install mysqlclient

    pip install --upgrade pip

    # 3. 使用しているlibrary 書き出し
    pip freeze > requirements.txt

    # 4. cloud SQL へ接続: 下記の command を使用して開発環境からアクセスできる
    memo.yaml 参照
    開発環境で MySQL につないで開発したい時は、terminal を１つ立ち上げて起動しておく事

    # 5. 新しく DB を立ち上げた状態で data がまだないので下記の command 実行
    # PORT で error 有った。instance=tcp:5432　の 5432 が PORT 番号
    python manage.py makemigrations
    python manage.py migrate

    # 6. My SQL の中に superuser 作成
    python manage.py createsuperuser

    # 7. runserver
    python manage.py runserver
- 記事一覧は MySQL では作成してないので何も表示されない
### 16-4. DataBase の接続ができたので本番環境も試す
    # app deploy
    gcloud app deploy --project moto-labo

    # browser で表示
    gcloud app browse

- yaml file の 改行や空白に注意！　error が起きる
- gcloud の command が聞かない時は、 source ~/.zshrc command を実行してから gcloud command 実行
- login して database が反映されているか確認！
### 16-5. Django 管理画面崩れ修正
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
> https://docs.djangoproject.com/ja/3.2/ref/contrib/staticfiles/
- settings.py に追記
  - **STATIC_ROOT**
    - collectstatic -> django 標準の管理画面の css(style) 静的file が上記の directory を作成する事によって作成される
    - 一緒に upload してくれる
### terminal
    # collectstatic : staticfile dir 作成
    python manage.py collectstatic
### app.yaml file 編集
    handlers:
    - url: /static
      static_dir: staticfiles/
- staticfiles に集めたので、本番環境は staticfiles から読み込むように修正
### もう一度 deploy して style があたっているか確認
    source ~/.zshrc
    gcloud app deploy --project moto-labo
### 16-6. .gcloudignore
- .gitignore と同じ
## 17. recaptcha 設定
> https://www.google.com/recaptcha/admin/create
- secret file に sitekey, secretkey を記述
> https://developers.google.com/recaptcha/docs/display
- template/mysite/contact.html に templat tag で {% include 'mysite/snippets/grecaptcha.html' %} 追記
  - snippets/ grecaptcha.html 作成・追記
### 17-1. grecaptcha.html 追記/ クライアント側の設定
    <script>
        // コールバック関数: reCAPTCHAをチェックしないと送信 button を押せないようにする
        function verfyCallback(response) {
            // submit の disabled 属性を解除
            document.getElementById(submit).disabled = false;
        }
    </script>
- reCAPTCHA をチェックすれば、送信 button が押せるようになる
1. mysite/views.py から sitekey を渡す contact 関数 context {} に記述
2. data-sitekey="{{ grecaptcha_sitekey }}"　template tag で記述
3. input に属性追加　required : 入力必須項目
### 17-2. reCAPTCHA server side の設定
- mysite/ views.py contact 関数に responce 後の code を記述
- RESTAPI を使用して裏でも検証をかける
## 18. GCS で画像 file を扱う
1. mysite/model/profile_model.py に class に image を追記
2. upload_image_to 関数を作成
#### 3. makemigrations -> migrate
    python manage.py makemigrations

    python -m pip install Pillow

    python manage.py migrate
4. mysite/forms.py の fields に image を追加
5. mysite/views.py mypage の関数に request.FILES を記述
   - user から送られてきた POST, FILES どちらも渡す為に記述
6.  account.html 下記を追記
    - < input type="file" class="form-control px-2" accept="image/*" id="id_image" name="image" />
### 18-1. GCS(Google Cloud Storage)
1. GCS でバケット作成
2. secret.yaml, secret_dev.yaml に GCS の変数になる KEY を記述
### 3. pip install 各種 library install
    # 1
    pip install django-storages

    # 2
    pip install google-cloud-storage

- django で簡単に接続してくれる library が含まれているもの
- document には AmazonAWS でも接続できるやりたが記述してある
- settings.py に GCS 設定項目を記述
## 19. class view
- mysite/views.py を編集
  - mypage と contact 関数を class view に変える
  - 汎用的なモノを使い、関数とクラスの違いを理解する
  - class に変更後は、 config の urls.py file path を変更する
  -
