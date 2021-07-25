from django.urls import path, include
from . import views  # . (dot)は blog dir の意


urlpatterns = [
    path('test/', views.test),
]
