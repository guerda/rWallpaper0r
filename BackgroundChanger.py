#!/usr/bin/python
# -*- coding: utf-8 -*-
import platform

class BackgroundChanger():
	SCHEMA = 'org.gnome.desktop.background'
	KEY = 'picture-uri'
	
	def change_background(self, filename):
		plat = self.detect_platform()
		if(plat == 'Ubuntu'):
			from gi.repository import Gtk, Gio
			gsettings = Gio.Settings.new(self.SCHEMA)
			print(gsettings.get_string(self.KEY))
			print(gsettings.set_string(self.KEY, "file://" + filename))
			print(gsettings.get_string(self.KEY))
			temp = Gtk.__dict__
			print(gsettings.get_string(self.KEY))
		elif(plat == 'Windows'):
			import ctypes
			SPI_SETDESKWALLPAPER = 20 
			ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, filename , 0)
		elif(plat == 'Mac'):
			print('Not yet implemented')
		else:
			print('Not yet implemented')

	def detect_platform(self):
		sys = platform.system()
		if(sys == 'Linux'):
			dist = platform.linux_distribution()
			if(dist[0]=='Ubuntu'):
				return dist[0]
		elif(sys == 'Windows'):
			return sys
		elif(sys == 'Darwin'):
			return 'Mac'

if __name__ == "__main__":
	#BackgroundChanger().change_background("/home/philip/Entwicklung/Python/rWallpaper0r/Eyes.jpg")
	print(BackgroundChanger().detect_platform())
