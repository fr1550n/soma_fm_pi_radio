#!/usr/bin/env python
from abc import ABC, abstractmethod
import subprocess
import time

# command abstract interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# command
class SomaCommand(Command):
    def __init__(self, media_player, station, screen):
        self.media_player = media_player
        self.station      = station
        self.screen       = screen

    def execute(self):
        print('execute: name:   ' + self.station.name.upper())
        print('execute: url:    ' + self.station.url)
        print('execute: colour: ' + str(self.station.colour))
        self.media_player.play(self.station.url)
        self.display(self.station)

    def display(self, station):
        self.screen.flash_backlight()
        self.screen.flash_buttons()
        self.screen.clear()
        self.screen.display("Soma FM", station.name)


class PausePlayCommand(Command):
        def __init__(self, media_player, station, screen):
            self.media_player = media_player
            self.station      = station
            self.screen       = screen

        def execute(self):
            self.media_player.toggle_play()


class ShutdownCommand(Command):
        def __init__(self, media_player, station, screen):
            self.media_player = media_player
            self.station      = station
            self.screen       = screen

        def execute(self):
            self.media_player.stop()
            self.screen.clear()
            self.screen.display("Shutting down", "zzzzz")
            time.sleep(3)
            self.screen.turn_off()
            time.sleep(3)
            subprocess.run(["sudo", "shutdown", "-h", "now"])