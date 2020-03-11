# Direct Server (Main)
debug = False

class RGB:
    """Colours!"""
    def __init__(self, red, green, blue):
        self.red   = red
        self.green = green
        self.blue  = blue
    def __str__(self):
        return "r:{} g:{} b:{}".format(self.red, self.green, self.blue)

class SomaFMStation:
    """Details about a soma fm radio station"""
    def __init__(self, name, url, colour):
        self.name   = name
        self.url    = url
        self.colour = colour
        if (debug):
            print("init: name: " + name + " url: " + url + " colour: " + colour)




class SomaFM:
    """Wrapper around SomaFM"""
    def __init__(self):
        self.stations = {'space_station': SomaFMStation(name='Space Station', url="http://ice6.somafm.com/spacestation-128-aac", colour=RGB(192, 192, 192)),
                         'drone_zone':    SomaFMStation(name='Drone Zone',    url="http://ice2.somafm.com/dronezone-128-aac",    colour=RGB(0,   51,  102)),
                         'groove_salad':  SomaFMStation(name='Groove Salad',  url="http://ice4.somafm.com/groovesalad-128-aac",  colour=RGB(0,   153, 76)),
                         'lush':          SomaFMStation(name='Lush',          url="http://ice6.somafm.com/lush-128-aac",         colour=RGB(255, 255, 153))}
    def listStations(self):
        for k in self.stations.keys():
            print("listStations: station: " + self.stations[k].name)