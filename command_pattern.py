#!/usr/bin/env python
from abc import ABC, abstractmethod
import signal
from gfxhat import touch
from soma_fm import SomaFM
from media_player import MediaPlayer

soma         = SomaFM()
media_player = MediaPlayer()

# command abstract interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# command
class SomaCommand(Command):
    def __init__(self, media_player, station):
        self.media_player = media_player,
        self.station      = station

    def execute(self):
        print('execute: name:   ' + self.station.name.upper())
        print('execute: url:    ' + self.station.url)
        print('execute: colour: ' + str(self.station.colour))
        media_player.play(self.station.url)


# my commands
up    = SomaCommand(media_player=media_player, station=soma.stations['space_station'])
down  = SomaCommand(media_player=media_player, station=soma.stations['drone_zone'])
left  = SomaCommand(media_player=media_player, station=soma.stations['groove_salad'])
minus = SomaCommand(media_player=media_player, station=soma.stations['lush'])
home  = SomaCommand(media_player=media_player, station=soma.stations['lush'])
plus  = SomaCommand(media_player=media_player, station=soma.stations['lush'])

# map channels (button index) to commands
buttonMappings = { 0: up,
                   1: down,
                   2: left,
                   3: minus,
                   4: home,
                   5: plus }

# command handler
def handler(channel, event):
    print("Got {} on channel {}".format(event, channel))
    buttonMappings[channel].execute()

# assign the command handler to the buttons
for x in range(6):
    touch.on(x, handler)


signal.pause() # https://docs.python.org/2/library/signal.html