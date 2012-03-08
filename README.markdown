rWallpaper0r
==
A simple wallpaper changer for Linux and Windows (propably MacOS, if you want).

Description
---
rWallpaper0r uses the fabulous community of [/r/wallpapers](http://reddit.com/r/wallpapers) to get a fresh and beautiful wallpaper directly on your desktop.
It changes the wallpaper directly after it was downloaded.

License
---
rWallpaper0r (not including the downloaded wallpapers) is published under the GPLv3 license or newer.

Installation
---
To run rWallpaper0r you need the following things:
### Linux ###
Python 3.2 (python3.2)
Python GOBjects (python3-gobject)
an Internet connection without blocking reddit.com and all image sources (99% imgur.com and deviantart.com)

Now just download rWallpaper0r and run

    ./rWallpaper0r.py

The magic line will find Python 3.2 (hopefully). If not, just run

    python3.2 rWallpaper0r.py
If you aliased python3.2 with python, you can run

    python rWallpaper0r.py

### Windows ###
The Windows branch is not developed correctly, so I don't know yet what is needed. Will come soon.

Known Issues
---
On Ubuntu 11.10, the wallpaper is not always updated. I don't know why, but the GObject interface does not give any hint why it does not update the wallpaper.
If somebody has an idea, just drop me a line.

Roadmap
---
I have a lot of ideas for the rWallpaper0r and here are some of them:
- Fixing known issues (this point will always stay here ;) )
- Implementing a GUI with progress bar and some configuration options
- Adding a NSFW (Not Suitable For Work) filter
- Adding a subreddit changer
- Adding a source hint on the wallpaper, if preferred, so that the originator of the wallpaper is known

Other Stuff
---
Have fun!
