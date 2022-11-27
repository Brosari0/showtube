from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'), 
    path('posts/index/', views.posts_index, name='index'),
    path('posts/create/', views.CreatePost.as_view(), name='create_post'),
    path('posts/<int:post_id>/', views.posts_detail, name='detail'),

    path('posts/<int:post_id>/comment/', views.add_comment, name='comment'),
]