import unittest
from rover import Rover
from rover import Direction

class RoverTest(unittest.TestCase):
    
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


if __name__ == '__main__':
    unittest.main()