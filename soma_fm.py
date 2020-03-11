# Direct Server (Main)
debug = False

class RGB:
    """Colours!"""
    def __init__(self, red, green, blue):
        self.red   = red
        self.green = green
        self.blue  = blue

class SomaFMStation:
    """Details about a soma fm radio station"""
    def __init__(self, name, url, colour):
        self.name   = name
        self.url    = url
        self.colour = colour
        if (debug):
            print("init: name: " + name + " url: " + url)




class SomaFM:
    """Wrapper around SomaFM"""
    def __init__(self):
        self.stations = [SomaFMStation(name='Space Station', url="http://ice6.somafm.com/spacestation-128-aac", RGB(192, 192, 192)),
                         SomaFMStation(name='Drone Zone',    url="http://ice2.somafm.com/dronezone-128-aac",    RGB(0,   51,  102)),
                         SomaFMStation(name='Groove Salad',  url="http://ice4.somafm.com/groovesalad-128-aac",  RGB(0,   153, 76)),
                         SomaFMStation(name='Lush',          url="http://ice6.somafm.com/lush-128-aac",         RGB(255, 255, 153)]



def listStations(somafm):
    for station in somafm.stations:
        print("listStations: station: " + station.name)

soma = SomaFM()
listStations(soma)