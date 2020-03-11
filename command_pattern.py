#!/usr/bin/env python
from abc import ABC, abstractmethod
import signal
from gfxhat import touch
from soma_fm import SomaFM

soma = SomaFM()
soma.listStations()

# command abstract interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# command
class SomaCommand(Command):
    def __init__(self, name):
        self.name = name
    def execute(self):
        print('execute:' + self.name.upper() + ' pressed')

# my commands
up    = SomaCommand('up')
down  = SomaCommand('down')
left  = SomaCommand('left')
minus = SomaCommand('minus')
home  = SomaCommand('home')
plus  = SomaCommand('plus')

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