import vlc
import time

url = 'http://ice6.somafm.com/groovesalad-128-aac'

#define VLC instance
#instance = vlc.Instance('--input-repeat=-1', '--fullscreen')

#Define VLC player
#player=instance.media_player_new()

#Define VLC media
#media=instance.media_new(url)

#Set player media
#player.set_media(media)

#Play the media
#player.play()

class MediaPlayer:
    """Wrapper around Video LAN Client"""
    def __init__(self):
        self.last_url = ""
        self.vlc      = vlc.Instance('--input-repeat=-1', '--fullscreen')
        self.player   = self.vlc.media_player_new()

    def play(self, url):
        if (url == self.last_url):
            pass
        self.last_url = url
        self.player.set_media(self.vlc.media_new(url))
        self.player.play()


#media_player=MediaPlayer()
#media_player.play(url)