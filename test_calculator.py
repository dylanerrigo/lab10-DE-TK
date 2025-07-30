#https://github.com/dylanerrigo/lab10-DE-TK.git
#Partner 1: Dylan Errigo
#Partner 2: Tristan Kerr
import unittest
import math
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(-5, 5), 0)
        self.assertEqual(calculator.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 5), 5)
        self.assertEqual(calculator.subtract(5, 10), -5)
        self.assertEqual(calculator.subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(calculator.mul(0, 1), 0)
        self.assertEqual(calculator.mul(1, 2), 2)
        self.assertEqual(calculator.mul(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(calculator.div(2, 1), 2)
        self.assertEqual(calculator.div(3, -1), -3)
        with self.assertRaises(ZeroDivisionError):
            calculator.div(3, 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(10, 0)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.log(10, 100), 2)
        self.assertAlmostEqual(calculator.log(math.e, math.e ** 5), 5)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.log(0, 10)
        with self.assertRaises(ValueError):
            calculator.log(1, 10)
        with self.assertRaises(ValueError):
            calculator.log(10, 0)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.log(0, 5)
        self.assertEqual(calculator.log(10, 10), 1)

    def test_hypotenuse(self):
        self.assertEqual(calculator.hypotenuse(3, 4), 5)
        self.assertEqual(calculator.hypotenuse(6, 8), 10)
        self.assertEqual(calculator.hypotenuse(1, 0), 1)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            calculator.square_root(-1)
        self.assertEqual(calculator.square_root(4), 2)
        self.assertEqual(calculator.square_root(0), 0)
        self.assertEqual(calculator.square_root(16), 4)

# Do not touch this
if __name__ == "__main__":
    unittest.main()