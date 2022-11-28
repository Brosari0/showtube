from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime


# Create your models here.
class Reaction(models.Model):
    url = models.CharField(max_length=500)

    def __str__(self):
        return self.url
    
    def get_absolute_url(self):
        return reverse('reactions_detail', kwargs={'pk': self.id})

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    youtube_url = models.URLField(max_length=255, null=True, blank=True)
    date = models.DateField('Post Date', default=datetime.now)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'post_id':self.id})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']


class Comment(models.Model):
    content = models.TextField(max_length=500, blank=True)
    date = models.DateField('Post Date', default=datetime.now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-date']