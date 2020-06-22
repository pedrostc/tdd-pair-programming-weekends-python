import unittest
from rover import Rover
from rover import Direction

class RoverTest(unittest.TestCase):
    
    ## CONDITION
    
    def test_receives_position_and_direction(self):
        rover = Rover(0, 0, Direction.NORTH)
        self.assertIsNotNone(rover)
        self.assertEqual(rover.x, 0)
        self.assertEqual(rover.y, 0)
        self.assertEqual(rover.direction.value, 'N')

    def test_validates_input_types(self):
        self.assertRaises(TypeError, lambda: Rover(0, 0, 'Pra La'))
        self.assertRaises(TypeError, lambda: Rover("bolinha", 0, Direction.NORTH))
        self.assertRaises(TypeError, lambda: Rover(0, "quadradinho", Direction.NORTH))
        
    ## TRANSLATION        
        
    def test_moves_forward_North(self):
        rover = Rover(0, 0, Direction.NORTH)
        rover.move(["F"])
        self.assertEqual(rover.y, 1)
        self.assertEqual(rover.x, 0)

    def test_moves_forward_South(self):
        rover = Rover(0, 0, Direction.SOUTH)
        rover.move(["F"])
        self.assertEqual(rover.y, -1)
        self.assertEqual(rover.x, 0)

    def test_moves_forward_East(self):
        rover = Rover(0, 0, Direction.EAST)
        rover.move(["F"])
        self.assertEqual(rover.y, 0)
        self.assertEqual(rover.x, 1)
    
    def test_moves_forward_West(self):
        rover = Rover(0, 0, Direction.WEST)
        rover.move(["F"])
        self.assertEqual(rover.y, 0)
        self.assertEqual(rover.x, -1)   

    def test_moves_backward_North(self):
        rover = Rover(0, 0, Direction.NORTH)
        rover.move(["B"])
        self.assertEqual(rover.y, -1)
        self.assertEqual(rover.x, 0)        

    def test_moves_backward_South(self):
        rover = Rover(0, 0, Direction.SOUTH)
        rover.move(["B"])
        self.assertEqual(rover.y, 1)
        self.assertEqual(rover.x, 0)       

    def test_moves_backward_East(self):
        rover = Rover(0, 0, Direction.EAST)
        rover.move(["B"])
        self.assertEqual(rover.y, 0)
        self.assertEqual(rover.x, -1)     

    def test_moves_backward_West(self):
        rover = Rover(0, 0, Direction.WEST)
        rover.move(["B"])
        self.assertEqual(rover.y, 0)
        self.assertEqual(rover.x, 1)  
            
## ROTATION
# TURN FROM NORTH
    def test_turns_left_North(self):
        rover = Rover(0, 0, Direction.NORTH)
        rover.move(["L"])
        self.assertEqual(rover.y, 0)
        self.assertEqual(rover.x, 0) 
        self.assertEqual(rover.direction, Direction.WEST)    

    def test_turns_right_North(self):
        rover = Rover(0, 0, Direction.NORTH)
        rover.move(["R"])
        self.assertEqual(rover.y, 0)
        self.assertEqual(rover.x, 0) 
        self.assertEqual(rover.direction, Direction.EAST)

# TURN FROM SOUTH
    def test_turns_left_South(self):
        rover = Rover(0, 0, Direction.SOUTH)
        rover.move(["L"])
        self.assertEqual(rover.y, 0)
        self.assertEqual(rover.x, 0) 
        self.assertEqual(rover.direction, Direction.EAST)    

    def test_turns_right_South(self):
        rover = Rover(0, 0, Direction.SOUTH)
        rover.move(["R"])
        self.assertEqual(rover.y, 0)
        self.assertEqual(rover.x, 0) 
        self.assertEqual(rover.direction, Direction.WEST) 

# TURN FROM EAST
    def test_turns_left_East(self):
        rover = Rover(0, 0, Direction.EAST)
        rover.move(["L"])
        self.assertEqual(rover.y, 0)
        self.assertEqual(rover.x, 0) 
        self.assertEqual(rover.direction, Direction.NORTH)    

    def test_turns_right_East(self):
        rover = Rover(0, 0, Direction.EAST)
        rover.move(["R"])
        self.assertEqual(rover.y, 0)
        self.assertEqual(rover.x, 0) 
        self.assertEqual(rover.direction, Direction.SOUTH) 

# TURN FROM WEST
    def test_turns_left_West(self):
        rover = Rover(0, 0, Direction.WEST)
        rover.move(["L"])
        self.assertEqual(rover.y, 0)
        self.assertEqual(rover.x, 0) 
        self.assertEqual(rover.direction, Direction.SOUTH)    

    def test_turns_right_West(self):
        rover = Rover(0, 0, Direction.WEST)
        rover.move(["R"])
        self.assertEqual(rover.y, 0)
        self.assertEqual(rover.x, 0) 
        self.assertEqual(rover.direction, Direction.NORTH)  


# MOVING AROUND
    def test_list_commands_from_west_Reach_End_Point(self):
        rover = Rover(0, 0, Direction.WEST)
        rover.move(["R" ,"R" ,"F" ,"F" ,"F" ,"F" ,"L" ,"L" ,"R" ,"B" ,"B", "R"])
        self.assertEqual(rover.y, -2)
        self.assertEqual(rover.x, 4) 
        self.assertEqual(rover.direction, Direction.EAST)

    # Start from here
    def test_Warp_around_grid(self):
        # TODO IMPLEMENT

if __name__ == '__main__':
    unittest.main()