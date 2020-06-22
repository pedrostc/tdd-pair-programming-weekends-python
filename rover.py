from enum import Enum
from rover_command import TranslationCommand, RotationCommand
from rover_base import RoverBase, Direction, Commands

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

class Rover(RoverBase):

    def __init__(self, x: int, y: int, direction: Direction):
        super().__init__(x, y, direction)

    def move(self, commands: list):
        for command in commands:
            self.move_single(Commands(command))

    def move_single(self, command: Commands):
        mutation = mutations[command][self.direction]

        mutation.applyTo(self)