from enum import Enum
from rover_command import TranslationCommand, RotationCommand
from rover_gps import RoverGps, Direction, Commands
from planet import PlanetMap

mutations = {
    Commands.FORWARD: {
        Direction.NORTH: TranslationCommand(0, 1),
        Direction.SOUTH: TranslationCommand(0, -1),
        Direction.EAST: TranslationCommand(1, 0),
        Direction.WEST: TranslationCommand(-1, 0)
    },

    Commands.BACKWARD: {
        Direction.NORTH: TranslationCommand(0, -1),
        Direction.SOUTH: TranslationCommand(0, 1),
        Direction.EAST: TranslationCommand(-1, 0),
        Direction.WEST: TranslationCommand(1, 0)
    },

    Commands.RIGHT : {
        Direction.NORTH: RotationCommand(Direction.EAST),
        Direction.SOUTH: RotationCommand(Direction.WEST),
        Direction.EAST: RotationCommand(Direction.SOUTH),
        Direction.WEST: RotationCommand(Direction.NORTH)
    },

    Commands.LEFT: {
        Direction.NORTH: RotationCommand(Direction.WEST),
        Direction.SOUTH: RotationCommand(Direction.EAST),
        Direction.EAST: RotationCommand(Direction.NORTH),
        Direction.WEST: RotationCommand(Direction.SOUTH)
    }
}

class Rover:

    def __init__(self, map: PlanetMap, x = 0, y = 0, direction = Direction.NORTH):
        self.gps = RoverGps(x, y, direction)

    def move(self, commands: list):
        for command in commands:
            self.move_single(Commands(command))           

    def move_single(self, command: Commands):
        mutation = mutations[command][self.gps.direction]

        mutation.applyTo(self.gps)

    def get_direction(self):
        return self.gps.direction

    def get_x(self):
        return self.gps.x

    def get_y(self):
        return self.gps.y
        