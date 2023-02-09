# -*- coding: utf-8 -*-
"""
This script download youtube video from playlist 

""" 
import sys
from pytube import YouTube 
from pytube import Playlist

link = input("Enter youTube playlist link: ")
save_folder = "/mnt/download/CCNA/"
pl = Playlist(link)
video_name = []
video_urls = pl.video_urls
video_items = pl.videos

#for i in video_items:
#    video_name.append(i.title)
#video_dict = dict(zip(video_name, video_urls))
#print(video_dict)



for url in pl.videos:
    try:
        print(f"Video: {url.title} | ",end="", flush=True)
        url.streams.get_highest_resolution().download(save_folder)
        print(f"saved")
    except:
        print(f"Error with video {url.title}") 
