import requests
import json, os
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
import googleapiclient.discovery 
import googleapiclient.errors
from .models import Post
from django.views.generic.edit import CreateView



DEVELOPER_KEY = os.environ['DEVELOPER_KEY']
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
    
class CreatePost(CreateView):
    model = Post
    fields = ['title', 'description', 'youtube_url']
    
    def form_valid(self, form):
    # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user
    # Let the CreateView do its job as usual (saving the object and redirecting)
        return super().form_valid(form)
