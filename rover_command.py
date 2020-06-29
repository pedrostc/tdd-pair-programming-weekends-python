from rover_gps import RoverGps
from rover_gps import Direction

class Command():
    def applyTo(self, rover: RoverGps):
        pass

class TranslationCommand(Command):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def applyTo(self, rover):
        rover.x += self.x
        rover.y += self.y

class RotationCommand(Command):
    def __init__(self, direction: Direction):
        self.direction = direction

    def applyTo(self, rover):
        rover.direction = self.direction