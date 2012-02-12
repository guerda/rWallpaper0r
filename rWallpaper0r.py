#!/usr/bin/python3.2
# -*- coding: utf-8 -*-
from wallpaper_url_fetcher import save_new_wallpaper
from BackgroundChanger import BackgroundChanger

filename = save_new_wallpaper()
print(filename)

changer = BackgroundChanger()
changer.change_background(filename)
print("Done")

