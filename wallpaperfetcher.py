#!/usr/bin/python3
# -*- coding: utf-8 -*-
import urllib.request, urllib.parse, urllib.error
import json
import mimetypes
from os import path
import os

class WallpaperFetcher():
    def __init__(self):
        self.WALLPAPER_DIR=("%s/%s")%(path.expanduser("~"),'Bilder/rWallpaper0r/')
        # check, if wallpaper dir exists. If not, create it.
        if not os.path.exists(self.WALLPAPER_DIR):
            os.makedirs(self.WALLPAPER_DIR)
        self.reddit_url='http://www.reddit.com/r/wallpapers/top/.json?sort=top&t=day'
        self.opener = urllib.request.build_opener()
        self.opener.addheaders = [('User-agent', 'rWallpaper0r/0.1')]
        mimetypes.init()

    def fetch_new_wallpaper_url(self):
        url = self.opener.open(self.reddit_url)
        data_bytes = url.read()
        json_string = str(data_bytes, "UTF-8")
        json_data = json.loads(json_string)
        i=0
        entry = json_data["data"]["children"][i]["data"]
        wallpaper_url = entry["url"]
        wallpaper_title = entry["title"]
        print(wallpaper_url[-3:])
        while wallpaper_url[-3:] != "jpg" and wallpaper_url[-4:] != "jpeg" \
                and wallpaper_url[-3:] != "png":
            entry = json_data["data"]["children"][i]["data"]
            wallpaper_url = entry["url"]
            wallpaper_title = entry["title"]
            print(wallpaper_url[-3:])
            i=i+1
        return [wallpaper_url, wallpaper_title]

    def fetch_new_wallpaper_data(self):
        url = self.opener.open(self.fetch_new_wallpaper_url()[0])
        data = ''
        for line in url:
	        data = data + line
        return data

    def save_new_wallpaper(self):
        wallpaper_data = self.fetch_new_wallpaper_url()
        data = self.opener.open(wallpaper_data[0])
        filename = str(wallpaper_data[1])
        mime_type = data.info().get_content_maintype()
        filename = filename.replace(" ", "").replace("\"", "")
        filename = filename.replace("'","").replace(",","").replace(".","")
        filename = filename.replace(":","").replace("?","")
        filename = filename.replace("[","").replace("]","")
        filename = filename.replace("(","").replace(")","")
        extension = mimetypes.guess_extension(mime_type)
        if(extension == ".jpe"):
            extension = ".jpg"
        elif(extension == None):
            extension = ""
        filename = "%s%s%s" % (self.WALLPAPER_DIR, filename, extension) 
        local_file = open(filename, "wb")
        local_file.write(data.read())
        local_file.close()
        return path.abspath(filename)

if __name__ == "__main__":
    fetcher = WallpaperFetcher()
    print(fetcher.save_new_wallpaper())
