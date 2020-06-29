from enum import Enum

class Direction(Enum):
    NORTH = "N" 
    SOUTH = "S" 
    EAST = "E" 
    WEST = "W" 

class Commands(Enum):
    FORWARD = "F"
    BACKWARD = "B"
    LEFT = "L"
    RIGHT = "R"

class RoverGps:

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