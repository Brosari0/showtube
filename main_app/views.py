import requests
import json, os
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Post, Comment, Reaction
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from .forms import CommentForm


# Create your views here.
def home(request):
    return render(request,'home.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - Try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)       
    
class CreatePost(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'description', 'youtube_url']
    def form_valid(self, form):
    # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user
    # Let the CreateView do its job as usual (saving the object and redirecting)
        return super().form_valid(form)
    
class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'description', 'youtube_url']

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/posts/index'
    
@login_required
def add_comment(request, post_id):
    form = CommentForm(request.POST)
    
    if form.is_valid():
        comment = form.save(commit=False)
        data = form.cleaned_data
        comment.content = data['content']
        comment.post_id = post_id
        comment.user_id = request.user.id
        comment.save()
    return redirect('detail', post_id=post_id)

class CommentUpdate(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ['content']

class CommentDelete(LoginRequiredMixin, DeleteView):
    model = Comment
    def get_success_url(self):
        return f"/posts/{self.object.post.id}"

def posts_index(request):
  posts = Post.objects.all()
  for post in posts:
    post.youtube_url = post.youtube_url.replace('watch?v=', 'embed/')
  return render(request, 'posts/index.html', {
    'posts': posts
  })

def posts_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post_id=post_id)
    post.youtube_url = post.youtube_url.replace('watch?v=', 'embed/')
    return render(request, 'posts/detail.html', {
        'post': post,
        'comments': comments
    })

class ReactionList(ListView):
    model = Reaction

class CreateReaction(LoginRequiredMixin, CreateView):
    model = Reaction
    fields = '__all__'

class ReactionDetail(LoginRequiredMixin, DetailView):
    model = Reaction

class ReactionUpdate(LoginRequiredMixin, UpdateView):
    model = Reaction
    fields = '__all__'

class ReactionDelete(LoginRequiredMixin, DeleteView):
    model = Reaction
    success_url = '/reactions'