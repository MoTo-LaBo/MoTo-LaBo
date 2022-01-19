from django.urls import path
from django.contrib.auth.views import LogoutView
from mysite import views


app_name = 'mysite'


urlpatterns = [
    path('', views.index, name='index'),
    path('identity/', views.identity, name='identity'),
    path('about/', views.about, name='about'),

    path('login/', views.Login.as_view()),
    path('logout/', LogoutView.as_view()),
    path('signup/', views.signup),
    path('account/', views.MypageView.as_view()),
    path('contact/', views.ContactView.as_view()),
    # path('pay/', views.PayView.as_view()),
    path('cache_test/', (views.cache_test)),

    # page の更新・生成があった場合の設定(Google にクロールに来て下さいと呼びかけ)
    path('ping/', views.ping),
]
