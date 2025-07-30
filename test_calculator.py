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

    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(0,1),0)
        self.assertEqual(mul(1,2),2)
        self.assertEqual(mul(-2,3),-6)
    def test_divide(self): # 3 assertions
        self.assertEqual(div(2,1),2)
        self.assertEqual(div(3,-1),-3)
        self.assertRaises(ZeroDivisionError,div,3,0)

        def test_logarithm(self):
            self.assertAlmostEqual(calculator.log(10, 100), 2)
            self.assertAlmostEqual(calculator.log(math.e, math.e ** 5), 5)


        def test_log_invalid_base(self):
            with self.assertRaises(ValueError):  # base <= 0
                calculator.log(0, 10)
            with self.assertRaises(ValueError):  # base == 1
                calculator.log(1, 10)
            with self.assertRaises(ValueError):  # value <= 0
                calculator.log(10, 0)

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