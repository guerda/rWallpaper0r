#!/usr/bin/python
# -*- coding: utf-8 -*-
from gi.repository import Gtk, Gio

class BackgroundChanger():
	SCHEMA = 'org.gnome.desktop.background'
	KEY = 'picture-uri'
	
	def change_background(self, filename):
		gsettings = Gio.Settings.new(self.SCHEMA)
		print(gsettings.get_string(self.KEY))
		print(gsettings.set_string(self.KEY, "file://" + filename))
		print(gsettings.get_string(self.KEY))
		temp = Gtk.__dict__

if __name__ == "__main__":
	BackgroundChanger().change_background("/home/philip/Entwicklung/Python/rWallpaper0r/Eyes.jpg")
