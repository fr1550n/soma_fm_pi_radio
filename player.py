#sudo apt-get install pulseaudio pulseaudio-module-zeroconf alsa-utils avahi-daemon
#sudo modprobe snd-bcm2835
#echo "snd-bcm2835" | sudo tee -a /etc/modules
#sudo nano /etc/pulse/default.pa
#pulseaudio -D
#sudo pulseaudio --system
# https://somafm.com/groovesalad/directstreamlinks.html

# sudo pip3 install vlc

#!/usr/bin/env python

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