#!/usr/bin/python
import urllib2
import json

reddit_url='http://www.reddit.com/r/wallpaper/top/.json?sort=top&t=day'
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'rWallpaper0r/0.1')]

def fetch_new_wallpaper_url():
	url = opener.open(reddit_url)
	data = ""
	for line in url:
		data = data + line + "\n"
	json_data = json.loads(data)
	return json_data["data"]["children"][0]["data"]["url"]

def fetch_new_wallpaper_data():
	url = opener.open(fetch_new_wallpaper_url())
	data = ''
	for line in url:
		data = data + line
	return data

if __name__ == "__main__":
	print(fetch_new_wallpaper_data())
