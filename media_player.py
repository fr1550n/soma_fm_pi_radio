import vlc

# define VLC instance
# instance = vlc.Instance('--input-repeat=-1', '--fullscreen')
# Define VLC player
# player=instance.media_player_new()
# Define VLC media
# media=instance.media_new(url)
# Set player media
# player.set_media(media)
# Play the media
# player.play()

class MediaPlayer:
    """Wrapper around Video LAN Client"""
    def __init__(self):
        self.last_url   = ""
        self.vlc        = vlc.Instance('--input-repeat=-1', '--fullscreen')
        self.player     = self.vlc.media_player_new()
        self.is_playing = False

    def play(self, url):
        # don't try to play the same url twice unless we've been stopped
        if (url != "" and url != self.last_url or not self.is_playing):
            self.last_url = url
            self.player.set_media(self.vlc.media_new(url))
            self.player.play()
            self.is_playing = True

    def stop(self):
        self.player.stop()
        self.is_playing = False

    def toggle_play(self):
        if self.is_playing:
            self.stop()
        else:
            self.play(self.last_url)

# url = 'http://ice6.somafm.com/groovesalad-128-aac'
# media_player=MediaPlayer()
# media_player.play(url)