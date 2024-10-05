import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method with various inputs."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(10.5, 2.2), 12.7)  # Test with floats
        self.assertEqual(self.calc.add(0, 0), 0)  # Test addition with zeros

    def test_subtraction(self):
        """Test the subtraction method with various inputs."""
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(1, -2), 3)
        self.assertEqual(self.calc.subtract(10.5, 2.2), 8.3)  # Test with floats
        self.assertEqual(self.calc.subtract(0, 0), 0)  # Test subtraction with zeros

    def test_multiplication(self):
        """Test the multiplication method with various inputs."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(10.5, 2), 21)  # Test with floats
        self.assertEqual(self.calc.multiply(1, 0), 0)  # Test multiplication with zero

    def test_division(self):
        """Test the division method with various inputs."""
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(10.5, 3), 3.5)  # Test with floats
        self.assertIsNone(self.calc.divide(10, 0))  # Test division by zero

if __name__ == '__main__':
    unittest.main()