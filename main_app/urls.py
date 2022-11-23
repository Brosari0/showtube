from django.urls import path
from . import views
from django.urls import re_path

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'), 
    path('posts/create/', views.CreatePost.as_view(), name='create_post'),
]