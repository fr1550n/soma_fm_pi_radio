#!/usr/bin/env python

# https://somafm.com/groovesalad/directstreamlinks.html

import vlc
import time

url = 'http://ice6.somafm.com/groovesalad-128-aac'

#define VLC instance
instance = vlc.Instance('--input-repeat=-1', '--fullscreen')

#Define VLC player
player=instance.media_player_new()

#Define VLC media
media=instance.media_new(url)

#Set player media
player.set_media(media)

#Play the media
player.play()