import unittest
import aoc14 

class TestConversion(unittest.TestCase):

    def test_to_int(self):
        i = "10011"
        expected = 19
        self.assertEqual(expected, aoc14.to_int(i), "wrong integer from string")
        i = "0"
        expected = 0
        self.assertEqual(expected, aoc14.to_int(i), "wrong integer from string")
        i = "0000"
        expected = 0
        self.assertEqual(expected, aoc14.to_int(i), "wrong integer from string")
    
    def test_to_str(self):
        i = 19
        expected = "10011"
        self.assertEqual(expected, aoc14.to_str(i), "wrong string-rep")
        i = 0
        expected = "0"
        self.assertEqual(expected, aoc14.to_str(i), "wrong string-rep")

    def test_to_str_wrt_bit(self):
        i = 9
        bit = 16
        expected = "0000000000001001"
        self.assertEqual(expected, aoc14.to_str_wrt_bits(i,bit=bit), "wrong string-rep wrt specified bit")

    def test_apply_mask(self):
        mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
        amount = 11
        expected = "000000000000000000000000000001001001"
        self.assertEqual(expected, aoc14.apply_mask(mask, amount), "mask applied incorrectly")

    def test_apply_mask_as_int(self):
        mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
        amount = 11
        expected = 73
        self.assertEqual(expected, aoc14.to_int(aoc14.apply_mask(mask, amount)), "mask applied wrong int")

    def test_apply_maskv2(self):
        mask = "000000000000000000000000000000X1001X"
        addr = 42
        expected = "000000000000000000000000000000X1101X"
        self.assertEqual(expected, aoc14.apply_mask_v2(mask, addr), "mask applied incorrectly")
    
    def test_get_addr_combos(self):
        expected = 2**8 #256
        wildcard_str = "10X1X0000111X11111X101X110111X11X00X"
        no_combos = len( aoc14.get_addr_combos(wildcard_str) )
        self.assertEqual(expected, no_combos, "all combination creation is wrong")


if __name__ == "__main__":
    unittest.main()