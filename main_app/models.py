from django.db import models
import argparse
from googleapiclient.discovery import build 
from googleapiclient.errors import HttpError
import json
import os
from collections import defaultdict
# Create your models here.
YOUTUBE_SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"

SAVE_PATH = f"{dir}/output"
class SearchVideo(models.Model):
    def __init__(self, searchTerm, maxResults, key):
        self.save_path = f"{SAVE_PATH}/search-keyword-csv"
        self.videos = defaultdict(list)
        self.params = {
            "q": searchTerm,
            "part":"id,snippet",
            "maxResults": maxResults,
            "key": key,
            }
        os.makedirs(self.save_path, exist_ok=True)
        
    def load_search_res(self, search_response):
        for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                self.videos["title"].append(search_result["snippet"]["title"])
                self.videos["description"].append(
                    search_result["snippet"]["description"]
                    )
                self.videos["publishedAt"].append(
                    search_result["snippet"]["publishedAt"]
                    )
                self.videos["channelTitle"].append(search_result["snippet"]["title"])
                self.videos["videoId"].append(search_result["id"]["videoId"])(
                    search_result["snippet"]["channelTitle"]
                    )
                    
            elif search_result["id"]["kind"] == "youtube#channel":
                self.channels["title"].append(search_result["snippet"]["title"])
                self.channels["description"].append(
                    search_result["snippet"]["description"]
                )
                self.channels["publishedAt"].append(
                    search_result["snippet"]["publishedAt"]
                )
                self.channels["channelId"].append(search_result["snippet"]["channelId"])

    