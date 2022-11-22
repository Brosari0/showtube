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
    
def search(request):
    videos = []
    query = request.GET.get('search')
    print(query)
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    response = requests.get(f"{search_url}?query={query}&key={DEVELOPER_KEY}").json()
    print(response)


    results = response['items']

    for result in results:   
        video_data = {
            'url': f'https://www.youtube.com/embed/{ result["id"]["videoId"] }',
            'id': result["id"]["videoId"]
        }
        videos.append(video_data)  
    print(videos)
    
    return render(request, 'posts/search.html', {'videos': videos})

class Create(CreateView):
    model = Post
    fields = ['title', 'description']
