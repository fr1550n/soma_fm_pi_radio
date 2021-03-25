#!/usr/bin/env python
from abc import ABC, abstractmethod
from command_pattern import SomaCommand, PausePlayCommand, ShutdownCommand
from soma_fm import SomaFM
from media_player import MediaPlayer
from screen import Screen
import signal
from gfxhat import touch

def main():
    soma         = SomaFM()
    media_player = MediaPlayer()
    screen       = Screen()

    # command handler
    # execute commands after finger has moved off of the button (the release event)
    def handler(channel, event):
        # print("Got {} on channel {}".format(event, channel))
        if event == "release":
            buttonMappings[channel].execute()

    # assign the command handler to the buttons
    for x in range(6):
        touch.on(x, handler)

    # my commands
    up    = SomaCommand(media_player=media_player, station=soma.stations['space_station'], screen=screen)
    down  = SomaCommand(media_player=media_player, station=soma.stations['drone_zone'], screen=screen)
    left  = SomaCommand(media_player=media_player, station=soma.stations['groove_salad'], screen=screen)
    minus = SomaCommand(media_player=media_player, station=soma.stations['lush'], screen=screen)
    home  = PausePlayCommand(media_player=media_player, station=soma.stations['lush'], screen=screen)
    plus  = ShutdownCommand(media_player=media_player, station=soma.stations['lush'], screen=screen)

    # map channels (button index) to commands
    buttonMappings = { 0: up,
                       1: down,
                       2: left,
                       3: minus,
                       4: home,
                       5: plus }
    signal.pause()  # https://docs.python.org/2/library/signal.html

if __name__ == "__main__":
    main()