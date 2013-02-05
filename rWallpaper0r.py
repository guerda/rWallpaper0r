#!/usr/bin/python3
# -*- coding: utf-8 -*-
from wallpaperfetcher import WallpaperFetcher
from backgroundchanger import BackgroundChanger
import sys

nsfw_filter = False
if(len(sys.argv) > 1):
    nsfw_filter = "--nsfw-filter" in (arg.lower() for arg in sys.argv)

filename = None
try:
	wp_fetcher = WallpaperFetcher()
	wp_fetcher.nsfw_filter = nsfw_filter
	filename = wp_fetcher.save_new_wallpaper()
	print(filename)
except Exception as e:
	print("Could not load Wallpaper: ",e)

changer = BackgroundChanger()
if(filename):
	changer.change_background(filename)
else:
	changer.set_random_background()
print("Done")

