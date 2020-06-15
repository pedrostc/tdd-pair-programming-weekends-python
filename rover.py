from enum import Enum

class Direction(Enum):
    NORTH = "N" 
    SOUTH = "S" 
    EAST = "E" 
    WEST = "W" 

class Rover:

    def __init__(self, x: int, y: int, direction: Direction):
        super().__init__()

        if not isinstance(direction, Direction):
            raise TypeError('Invalid direction!')

        if not isinstance(x, int):
            raise TypeError('x NaN')

        if not isinstance(y, int):
            raise TypeError('y NaN')

        self.x = x
        self.y = y
        self.direction = direction


    def move(self, commands: list):
        for command in commands:
            self.move_single(command)

    def move_single(self, command: str):
        if  command == "F":
            if self.direction == Direction.NORTH:
                self.y += 1

            if self.direction == Direction.SOUTH:
                self.y -= 1

            if self.direction == Direction.EAST:
                self.x += 1

            if self.direction == Direction.WEST:
                self.x -= 1               

        elif  command == "B":
            if self.direction == Direction.NORTH:
                self.y -= 1
