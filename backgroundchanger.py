#!/usr/bin/python3
# -*- coding: utf-8 -*-
import platform

class BackgroundChanger():
	SCHEMA = 'org.gnome.desktop.background'
	KEY = 'picture-uri'
	
	def change_background(self, filename):
		plat = self.detect_platform()
		if(plat == 'Ubuntu' or plat == 'Fedora'):
			from gi.repository import Gtk, Gio
			Gtk.Window()
			gsettings = Gio.Settings.new(self.SCHEMA)
			print(gsettings.get_string(self.KEY))
			print(gsettings.set_string(self.KEY, "file://" + filename))
			print(gsettings.get_string(self.KEY))
			print(gsettings.get_string(self.KEY))
			Gtk.Window()
			gsettings = None
			gsettings = Gio.Settings.new(self.SCHEMA)
			print(gsettings.get_string(self.KEY))
			import os
			latestlink = os.path.dirname(filename)+"/latest"
			if os.path.islink(latestlink):
				os.unlink(latestlink)
			os.symlink(filename, latestlink)
		elif(plat == 'Windows'):
			import ctypes
			# See http://msdn.microsoft.com/en-us/library/ms724947%28VS.85%29.aspx for details
			SPI_SETDESKWALLPAPER = 0x0014 
			cbuffer = ctypes.c_buffer(str.encode(filename))
			result = ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 1,  cbuffer, 1)
			if not result:
				print('Failed to set Wallpaper')
		elif(plat == 'Mac'):
			print('Not yet implemented for Mac')
		else:
			print('Not yet implemented for',plat)

	def detect_platform(self):
		sys = platform.system()
		if(sys == 'Linux'):
			dist = platform.linux_distribution()
			return dist[0]
		elif(sys == 'Windows'):
			return sys
		elif(sys == 'Darwin'):
			return 'Mac'
			
	def set_random_background(self):
		import glob
		import random
		from os import path
		path = ("%s/%s")%(path.expanduser("~"),'Bilder/rWallpaper0r/') # TODO Externalize
		files  = glob.glob(path+'\*')
		choice = random.choice(files)
		self.change_background(choice)

if __name__ == "__main__":
	print(BackgroundChanger().detect_platform())
	BackgroundChanger().set_random_background()
