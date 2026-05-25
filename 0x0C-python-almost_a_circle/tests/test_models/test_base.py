#!/usr/bin/python3
"""Test cases for the Base class."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unittests for testing the Base class."""

    def test_no_id(self):
        """Test assigning id automatically."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_custom_id(self):
        """Test assigning a custom id."""
        b3 = Base(89)
        self.assertEqual(b3.id, 89)

    def test_id_after_custom(self):
        """Test auto id after a custom id was assigned."""
        b4 = Base()
        self.assertEqual(b4.id, 3)


if __name__ == '__main__':
    unittest.main()
