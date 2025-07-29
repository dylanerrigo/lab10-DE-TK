#https://github.com/dylanerrigo/lab10-DE-TK.git
#Partner 1: Dylan Errigo
#Partner 2: Tristan Kerr
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(0,1),0)
        self.assertEqual(mul(1,2),2)
        self.assertEqual(mul(-2,3),-6)
    def test_divide(self): # 3 assertions
        self.assertEqual(div(2,1),2)
        self.assertEqual(div(3,-1),-3)
        self.assertRaises(ZeroDivisionError,div,3,0)
    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaise(ValueError):
            log(0,5)
        self.assertEqual(log(10,10),1)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4),5)
        self.assertEqual(hypotenuse(6,8),10)
        self.assertEqual(hypotenuse(1,0),1)
    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(4),2)
        self.assertEqual(square_root(0),0)
        self.assertEqual(square_root(16),4)

# Do not touch this
if __name__ == "__main__":
    unittest.main()