from django.urls import path
from . import views
from django.urls import re_path

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('posts/search/', views.search, name='search'),
  
    path('posts/create/<str:video_id>', views.Create.as_view(), name='create'),
    #re_path(r'posts/create/(?P<post_id>[0-9]+)/$', views.Create.as_view(), name='create'),


]