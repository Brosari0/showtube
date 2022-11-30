from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'), 
    path('posts/index/', views.posts_index, name='index'),
    path('posts/create/', views.CreatePost.as_view(), name='create_post'),
    path('posts/<int:post_id>/', views.posts_detail, name='detail'),
    path('posts/<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
    path('posts/<int:post_id>/comment/', views.add_comment, name='comment'),
    path('posts/<int:post_id>/update/<int:pk>/', views.CommentUpdate.as_view(), name='comment_update'),
    path('posts/<int:post>/delete/<int:pk>/', views.CommentDelete.as_view(), name='comment_delete'),
    
    path('reactions/', views.ReactionList.as_view(), name='reactions_index'),
    path('reactions/<int:pk>/', views.ReactionDetail.as_view(), name='reactions_detail'),
    path('reactions/create/', views.CreateReaction.as_view(), name='create_reaction'),
    path('reactions/<int:pk>/update', views.ReactionUpdate.as_view(), name='reactions_update'),
    path('reactions/<int:pk>/delete', views.ReactionDelete.as_view(), name='reactions_delete'),
]