from django.urls import path, include
from . import views  # . (dot)は blog dir の意


app_name = 'blog'


urlpatterns = [
    # path('test/', views.test),
    path('articles/', views.articles_list),
    path('tags/<slug:slug>/', views.tags),
    path('<slug:pk>/', views.article, name='article'),
    path('<slug:pk>/like/', views.like),
]
