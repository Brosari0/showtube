from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_id = models.CharField(max_length=255, unique=True, null=True,
                                help_text=("The Youtube id of the video"))
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    keywords = models.CharField(max_length=200, null=True, blank=True,
                                help_text=("Comma seperated keywords"))
    youtube_url = models.URLField(max_length=255, null=True, blank=True)


    def get_absolute_url(self):
        return self.url

# class Thumbnail(models.Model):
#     video = models.ForeignKey(Video, null=True)
#     url = models.URLField(max_length=255)

#     def __unicode__(self):
#         return self.url

#     def get_absolute_url(self):
#         return self.url
