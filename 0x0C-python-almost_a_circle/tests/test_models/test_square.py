#!/usr/bin/python3
"""Test cases for the Square class."""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Unittests for testing the Square class."""

    def test_area(self):
        """Test area calculation."""
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

    def test_size_validation(self):
        """Test size validation (must be int)."""
        with self.assertRaises(TypeError):
            Square("5")

    def test_size_value(self):
        """Test size validation (must be > 0)."""
        with self.assertRaises(ValueError):
            Square(-5)

    def test_str(self):
        """Test __str__ output."""
        s1 = Square(5, 1, 1, 12)
        self.assertEqual(str(s1), "[Square] (12) 1/1 - 5")


if __name__ == '__main__':
    unittest.main()
