#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import json
import mimetypes
from os import path

reddit_url='http://www.reddit.com/r/wallpaper/top/.json?sort=top&t=day'
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'rWallpaper0r/0.1')]
mimetypes.init()


def fetch_new_wallpaper_url():
	url = opener.open(reddit_url)
	data = ""
	for line in url:
		data = data + line + "\n"
	json_data = json.loads(data)
	first_entry = json_data["data"]["children"][0]["data"]
	wallpaper_url = first_entry["url"]
	wallpaper_title = first_entry["title"]
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
	filename = filename.replace(" ", "_").replace("\"", "").replace("'","").replace(",","")
	filename = "%s%s" % (filename, mimetypes.guess_extension(mime_type))
	local_file = open(filename, "wb")
	local_file.write(data.read())
	local_file.close()
	return path.abspath(filename)

if __name__ == "__main__":
	print(save_new_wallpaper())
