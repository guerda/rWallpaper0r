#!/usr/bin/python3
# -*- coding: utf-8 -*-
from wallpaperfetcher import WallpaperFetcher
from backgroundchanger import BackgroundChanger
import sys

nsfw_filter = False
if(len(sys.argv) > 1):
    nsfw_filter = "--nsfw-filter" in (arg.lower() for arg in sys.argv)

wp_fetcher = WallpaperFetcher()
wp_fetcher.nsfw_filter = nsfw_filter
filename = wp_fetcher.save_new_wallpaper()
print(filename)

changer = BackgroundChanger()
changer.change_background(filename)
print("Done")

