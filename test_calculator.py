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
if __name__ == "__main__":
    unittest.main()