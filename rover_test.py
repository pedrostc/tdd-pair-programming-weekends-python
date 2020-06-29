import unittest
from rover import Rover
from rover import Direction
from planet import PlanetMap

class RoverTest(unittest.TestCase):
    
    ## CONDITION
    
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
        
    ## TRANSLATION        
        
    def test_moves_forward_North(self):
        map = PlanetMap(10,10)
        rover = Rover(map, 0, 0, Direction.NORTH)
        rover.move(["F"])
        self.assertEqual(rover.get_y(), 1)
        self.assertEqual(rover.get_x(), 0)

    def test_moves_forward_South(self):
        map = PlanetMap(10,10)
        rover = Rover(map, 0, 0, Direction.SOUTH)
        rover.move(["F"])
        self.assertEqual(rover.get_y(), -1)
        self.assertEqual(rover.get_x(), 0)

    def test_moves_forward_East(self):
        map = PlanetMap(10,10)
        rover = Rover(map, 0, 0, Direction.EAST)
        rover.move(["F"])
        self.assertEqual(rover.get_y(), 0)
        self.assertEqual(rover.get_x(), 1)
    
    def test_moves_forward_West(self):
        map = PlanetMap(10,10)
        rover = Rover(map, 0, 0, Direction.WEST)
        rover.move(["F"])
        self.assertEqual(rover.get_y(), 0)
        self.assertEqual(rover.get_x(), -1)   

    def test_moves_backward_North(self):
        map = PlanetMap(10,10)
        rover = Rover(map, 0, 0, Direction.NORTH)
        rover.move(["B"])
        self.assertEqual(rover.get_y(), -1)
        self.assertEqual(rover.get_x(), 0)        

    def test_moves_backward_South(self):
        map = PlanetMap(10,10)
        rover = Rover(map, 0, 0, Direction.SOUTH)
        rover.move(["B"])
        self.assertEqual(rover.get_y(), 1)
        self.assertEqual(rover.get_x(), 0)       

    def test_moves_backward_East(self):
        map = PlanetMap(10,10)
        rover = Rover(map, 0, 0, Direction.EAST)
        rover.move(["B"])
        self.assertEqual(rover.get_y(), 0)
        self.assertEqual(rover.get_x(), -1)     

    def test_moves_backward_West(self):
        map = PlanetMap(10,10)
        rover = Rover(map, 0, 0, Direction.WEST)
        rover.move(["B"])
        self.assertEqual(rover.get_y(), 0)
        self.assertEqual(rover.get_x(), 1)  
            
## ROTATION
# TURN FROM NORTH
    def test_turns_left_North(self):
        map = PlanetMap(10,10)
        rover = Rover(map, 0, 0, Direction.NORTH)
        rover.move(["L"])
        self.assertEqual(rover.get_y(), 0)
        self.assertEqual(rover.get_x(), 0) 
        self.assertEqual(rover.get_direction(), Direction.WEST)    

    def test_turns_right_North(self):
        map = PlanetMap(10,10)
        rover = Rover(map, 0, 0, Direction.NORTH)
        rover.move(["R"])
        self.assertEqual(rover.get_y(), 0)
        self.assertEqual(rover.get_x(), 0) 
        self.assertEqual(rover.get_direction(), Direction.EAST)

# TURN FROM SOUTH
    def test_turns_left_South(self):
        map = PlanetMap(10,10)
        rover = Rover(map, 0, 0, Direction.SOUTH)
        rover.move(["L"])
        self.assertEqual(rover.get_y(), 0)
        self.assertEqual(rover.get_x(), 0) 
        self.assertEqual(rover.get_direction(), Direction.EAST)    

    def test_turns_right_South(self):
        map = PlanetMap(10,10)
        rover = Rover(map, 0, 0, Direction.SOUTH)
        rover.move(["R"])
        self.assertEqual(rover.get_y(), 0)
        self.assertEqual(rover.get_x(), 0) 
        self.assertEqual(rover.get_direction(), Direction.WEST) 

# TURN FROM EAST
    def test_turns_left_East(self):
        map = PlanetMap(10,10)
        rover = Rover(map, 0, 0, Direction.EAST)
        rover.move(["L"])
        self.assertEqual(rover.get_y(), 0)
        self.assertEqual(rover.get_x(), 0) 
        self.assertEqual(rover.get_direction(), Direction.NORTH)    

    def test_turns_right_East(self):
        map = PlanetMap(10,10)
        rover = Rover(map, 0, 0, Direction.EAST)
        rover.move(["R"])
        self.assertEqual(rover.get_y(), 0)
        self.assertEqual(rover.get_x(), 0) 
        self.assertEqual(rover.get_direction(), Direction.SOUTH) 

# TURN FROM WEST
    def test_turns_left_West(self):
        map = PlanetMap(10,10)
        rover = Rover(map, 0, 0, Direction.WEST)
        rover.move(["L"])
        self.assertEqual(rover.get_y(), 0)
        self.assertEqual(rover.get_x(), 0) 
        self.assertEqual(rover.get_direction(), Direction.SOUTH)    

    def test_turns_right_West(self):
        map = PlanetMap(10,10)
        rover = Rover(map, 0, 0, Direction.WEST)
        rover.move(["R"])
        self.assertEqual(rover.get_y(), 0)
        self.assertEqual(rover.get_x(), 0) 
        self.assertEqual(rover.get_direction(), Direction.NORTH)  


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
    
    def test_map_identify_vertical_border(self):
        self.assertEqual(True, False)


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