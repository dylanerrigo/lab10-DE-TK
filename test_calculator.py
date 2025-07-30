#https://github.com/dylanerrigo/lab10-DE-TK.git
#Partner 1: Dylan Errigo
#Partner 2: Tristan Kerr
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    import unittest
    import math
    import calculator

    class TestCalculator(unittest.TestCase):

<<<<<<< HEAD
        def test_add(self):
            self.assertEqual(calculator.add(1, 2), 3)
            self.assertEqual(calculator.add(-5, 5), 0)
            self.assertEqual(calculator.add(0, 0), 0)

        def test_subtract(self):
            self.assertEqual(calculator.sub(10, 5), 5)
            self.assertEqual(calculator.sub(5, 10), -5)
            self.assertEqual(calculator.sub(0, 0), 0)

        def test_divide_by_zero(self):
            with self.assertRaises(ZeroDivisionError):
                calculator.div(10, 0)
=======
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
>>>>>>> fb57cff168390e10965c0778728b941c5b821347

        def test_logarithm(self):
            self.assertAlmostEqual(calculator.log(10, 100), 2)
            self.assertAlmostEqual(calculator.log(math.e, math.e ** 5), 5)

<<<<<<< HEAD
        def test_log_invalid_base(self):
            with self.assertRaises(ValueError):  # base <= 0
                calculator.log(0, 10)
            with self.assertRaises(ValueError):  # base == 1
                calculator.log(1, 10)
            with self.assertRaises(ValueError):  # value <= 0
                calculator.log(10, 0)
=======
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