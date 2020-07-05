import unittest
from rover import Rover
from rover import Direction
from planet import PlanetMap
from parameterized import parameterized

class RoverTest(unittest.TestCase):
    
    # CONDITION
    def test_receives_position_direction_and_map(self):
        map = PlanetMap(10,10)
        rover = Rover(map, 0, 0, Direction.NORTH)
        self.assertIsNotNone(rover)
        self.assertEqual(rover.get_x(), 0)
        self.assertEqual(rover.get_y(), 0)
        self.assertEqual(rover.get_direction().value, 'N')

    def test_validates_input_types(self):
        self.assertRaises(TypeError, lambda: Rover(0, 0, 'Pra La'))
        self.assertRaises(TypeError, lambda: Rover("bolinha", 0, Direction.NORTH))
        self.assertRaises(TypeError, lambda: Rover(0, "quadradinho", Direction.NORTH))
        
    # TRANSLATION

    @parameterized.expand([
        ("moving FORWARD facing NORTH", Direction.NORTH, "F", 0, 1),
        ("moving FORWARD facing SOUTH", Direction.SOUTH, "F", 0, -1),
        ("moving FORWARD facing EAST", Direction.EAST, "F", 1, 0),
        ("moving FORWARD facing WEST", Direction.WEST, "F", -1, 0),
        ("moving BACKWARDS facing NORTH", Direction.NORTH, "B", 0, -1),
        ("moving BACKWARDS facing SOUTH", Direction.SOUTH, "B", 0, 1),
        ("moving BACKWARDS facing EAST", Direction.EAST, "B", -1, 0),
        ("moving BACKWARDS facing WEST", Direction.WEST, "B", 1, 0),        
    ])
    def test_translation(self, _, direction, command, expectedX, expectedY):
        map = PlanetMap(10,10)
        rover = Rover(map, 0, 0, direction)
        rover.move([command])
        self.assertEqual(rover.get_x(), expectedX)
        self.assertEqual(rover.get_y(), expectedY)     
            
## ROTATION
# TURN FROM NORTH
    @parameterized.expand([
        ("turning RIGHT from NORTH", Direction.NORTH, "R", Direction.EAST),
        ("turning LEFT from NORTH", Direction.NORTH, "L", Direction.WEST),
        ("turning RIGHT from SOUTH", Direction.SOUTH, "R", Direction.WEST),
        ("turning LEFT from SOUTH", Direction.SOUTH, "L", Direction.EAST),
        ("turning RIGHT from EAST", Direction.EAST, "R", Direction.SOUTH),
        ("turning LEFT from EAST", Direction.EAST, "L", Direction.NORTH),
        ("turning RIGHT from WEST", Direction.WEST, "R", Direction.NORTH),
        ("turning LEFT from WEST", Direction.WEST, "L", Direction.SOUTH),
    ])
    def test_rotation(self, _, originalDirection, command, expectedDirection):
        map = PlanetMap(10,10)
        rover = Rover(map, 0, 0, originalDirection)
        rover.move([command])
        self.assertEqual(rover.get_y(), 0)
        self.assertEqual(rover.get_x(), 0) 
        self.assertEqual(rover.get_direction(), expectedDirection)

# MOVING AROUND
    def test_list_commands_from_west_Reach_End_Point(self):
        map = PlanetMap(10,10)
        rover = Rover(map, 0, 0, Direction.WEST)
        rover.move(["R" ,"R" ,"F" ,"F" ,"F" ,"F" ,"L" ,"L" ,"R" ,"B" ,"B", "R"])
        self.assertEqual(rover.get_y(), -2)
        self.assertEqual(rover.get_x(), 4) 
        self.assertEqual(rover.get_direction(), Direction.EAST)

    # Start from here
    def test_map_can_map(self):
        planet_map = PlanetMap(2, 2)
        self.assertEqual(planet_map.get_height(), 2)
        self.assertEqual(planet_map.get_width(), 2)

    def test_map_identify_horizontal_border(self):
        # given a 2x2 planet
        planet_map = PlanetMap(2,2)
        # when checking a point pair on the edge
        isEdge = planet_map.is_edge(1, 0)
        # identify the edge
        self.assertEqual(isEdge, True)
    
    # def test_map_identify_vertical_border(self):
    #     self.assertEqual(True, False)


    # def test_Warp_around_grid(self):
    #     # given a 2x2 planet
    #     planet_map = PlanetMap(2,2)
    #     # and a rover on the right border facing east
    #     rover = Rover(planet_map, 1, 0, Direction.EAST)

    #     #when moving forward
    #     rover.move(["F"])

    #     #rover Moves to the left edge facing east
    #     self.assertEqual(rover.get_x(), -1)


if __name__ == '__main__':
    unittest.main()