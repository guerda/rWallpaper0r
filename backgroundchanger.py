#!/usr/bin/python3.2
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
			SPI_SETDESKWALLPAPER = 20 
			ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, filename , 0)
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

if __name__ == "__main__":
	print(BackgroundChanger().detect_platform())
