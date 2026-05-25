#!/usr/bin/python3
"""Test cases for the Rectangle class."""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Unittests for testing the Rectangle class."""

    def test_area(self):
        """Test area calculation."""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

    def test_width_validation(self):
        """Test width validation (must be int)."""
        with self.assertRaises(TypeError):
            Rectangle("10", 2)

    def test_width_value(self):
        """Test width validation (must be > 0)."""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_x_validation(self):
        """Test x validation (must be >= 0)."""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1)

    def test_str(self):
        """Test __str__ output."""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")


if __name__ == '__main__':
    unittest.main()
