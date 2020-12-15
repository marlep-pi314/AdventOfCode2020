import unittest
import aoc12 

class TestNavigation(unittest.TestCase):

    def test_get_total(self):
        total = aoc12.get_total("test_input")
        self.assertEqual(25, total, "wrong total")
    
    def test_facing(self):
        ferry = aoc12.Ferry()
        self.assertEqual('E', ferry.is_facing(), "default facing wrong")

    def test_turn_90left(self):
        ferry = aoc12.Ferry()
        ferry.move('L',90)
        self.assertEqual('N', ferry.is_facing(), "turn left 90 wrong")

    def test_turn_180right(self):
        ferry = aoc12.Ferry()
        ferry.move('R',180)
        self.assertEqual('W', ferry.is_facing(), "turn right 180 wrong")
    
    def test_move_north_20(self):
        ferry = aoc12.Ferry()
        ferry.move('N', 20)
        self.assertEqual({'N':20, 'E':0}, ferry.pos, "move north wrong")
    
    def test_movement(self):
        ferry = aoc12.Ferry()
        moves =[('N',10), ('W',100), ('S',10), ('E',50)]
        for d, a in moves:
            ferry.move(d, a)
        final_dest = {
            'N' : 0,
            'E' : -50
        }
        self.assertEqual(final_dest, ferry.pos, "movement failed")

if __name__ == "__main__":
    unittest.main()