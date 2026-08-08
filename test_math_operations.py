import unittest
from math_operations import factorial

class TestFactorial(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(factorial(5), 120)

    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_one(self):
        self.assertEqual(factorial(1), 1)

    def test_negative_integer(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            factorial(1.5)
        with self.assertRaises(TypeError):
            factorial("hello")

if __name__ == '__main__':
    unittest.main()