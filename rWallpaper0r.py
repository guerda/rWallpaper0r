#!/usr/bin/python3
# -*- coding: utf-8 -*-
from wallpaperfetcher import WallpaperFetcher
from backgroundchanger import BackgroundChanger

wp_fetcher = WallpaperFetcher()
filename = wp_fetcher.save_new_wallpaper()
print(filename)

changer = BackgroundChanger()
changer.change_background(filename)
print("Done")

