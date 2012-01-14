#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import json
import mimetypes
from os import path

WALLPAPER_DIR=("%s/%s")%(path.expanduser("~"),'Bilder/rWallpaper0r/')
reddit_url='http://www.reddit.com/r/wallpapers/top/.json?sort=top&t=day'
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'rWallpaper0r/0.1')]
mimetypes.init()


def fetch_new_wallpaper_url():
	url = opener.open(reddit_url)
	data = ""
	for line in url:
		data = data + line + "\n"
	json_data = json.loads(data)
	i=0
	entry = json_data["data"]["children"][i]["data"]
	wallpaper_url = entry["url"]
	wallpaper_title = entry["title"]
	print(wallpaper_url[-3:])
	while wallpaper_url[-3:] <> "jpg" and wallpaper_url[-4:] <> "jpeg" and wallpaper_url[-3:] <> "png":
		entry = json_data["data"]["children"][i]["data"]
		wallpaper_url = entry["url"]
		wallpaper_title = entry["title"]
		print(wallpaper_url[-3:])
		i=i+1
	return [wallpaper_url, wallpaper_title]

def fetch_new_wallpaper_data():
	url = opener.open(fetch_new_wallpaper_url()[0])
	data = ''
	for line in url:
		data = data + line
	return data

def save_new_wallpaper():
	wallpaper_data = fetch_new_wallpaper_url()
	data = opener.open(wallpaper_data[0])
	filename = unicode(wallpaper_data[1])
	mime_type = data.info().gettype()
	filename = filename.replace(" ", "_").replace("\"", "").replace("'","").replace(",","").replace(".","_").replace(":","_").replace("?","_")
	extension = mimetypes.guess_extension(mime_type)
	if(extension == ".jpe"):
		extension = ".jpg"
	filename = "%s%s%s" % (WALLPAPER_DIR, filename, extension) 
	local_file = open(filename, "wb")
	local_file.write(data.read())
	local_file.close()
	return path.abspath(filename)

if __name__ == "__main__":
	print(save_new_wallpaper())
