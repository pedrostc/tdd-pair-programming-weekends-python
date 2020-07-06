from rover_gps import RoverGps
from rover_gps import Direction
from planet import PlanetMap

class Command():
    def applyTo(self, roverGps: RoverGps, map: PlanetMap):
        pass

class TranslationCommand(Command):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def applyTo(self, roverGps, map: PlanetMap):
        roverGps.x = self.resolveNewX(roverGps, map)
        roverGps.y = self.resolveNewY(roverGps, map)

    def resolveNewY(self, roverGps, map: PlanetMap):
        tempY = roverGps.y
        tempY += self.y

        if (tempY < 0):
            tempY = map.get_max_y()
        elif (tempY > map.get_max_y()):
            tempY = 0
        
        return tempY

    def resolveNewX(self, roverGps, map: PlanetMap):
        tempX = roverGps.x
        tempX += self.x

        if (tempX < 0):
            tempX = map.get_max_x()
        elif (tempX > map.get_max_x()):
            tempX = 0
        
        return tempX

class RotationCommand(Command):
    def __init__(self, direction: Direction):
        self.direction = direction

    def applyTo(self, roverGps, map: PlanetMap):
        roverGps.direction = self.direction