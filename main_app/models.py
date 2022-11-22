from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_id = models.CharField(max_length=255, unique=True, null=True,
                                help_text=("The Youtube id of the video"))
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    youtube_url = models.URLField(max_length=255, null=True, blank=True)
    comment = models.CharField(max_length=100, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('posts_detail', kwargs={'pk':self.id})

