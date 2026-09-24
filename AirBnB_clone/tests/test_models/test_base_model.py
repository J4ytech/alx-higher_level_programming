#!/usr/bin/python3
"""Unit tests for BaseModel."""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests for the BaseModel class."""

    def test_instance_creation(self):
        """Test BaseModel instance creation."""
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

    def test_id_exists(self):
        """Test that id exists."""
        obj = BaseModel()
        self.assertIn("id", obj.__dict__)

    def test_id_is_string(self):
        """Test that id is a string."""
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)

    def test_dates_exist(self):
        """Test created_at and updated_at."""
        obj = BaseModel()
        self.assertIn("created_at", obj.__dict__)
        self.assertIn("updated_at", obj.__dict__)

    def test_dates_are_datetime(self):
        """Test created_at and updated_at are datetime objects."""
        obj = BaseModel()
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_two_objects_have_different_ids(self):
        """Test each object has a unique id."""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_save_updates_updated_at(self):
        """Test save updates updated_at."""
        obj = BaseModel()
        old_time = obj.updated_at

        obj.save()

        self.assertNotEqual(old_time, obj.updated_at)

    def test_to_dict_returns_dictionary(self):
        """Test to_dict returns a dictionary."""
        obj = BaseModel()
        self.assertIsInstance(obj.to_dict(), dict)

    def test_to_dict_contains_class_name(self):
        """Test __class__ key exists."""
        obj = BaseModel()
        obj_dict = obj.to_dict()

        self.assertIn("__class__", obj_dict)
        self.assertEqual(obj_dict["__class__"], "BaseModel")

    def test_to_dict_dates_are_strings(self):
        """Test datetime values become strings."""
        obj = BaseModel()
        obj_dict = obj.to_dict()

        self.assertIsInstance(obj_dict["created_at"], str)
        self.assertIsInstance(obj_dict["updated_at"], str)

    def test_str_returns_string(self):
        """Test __str__ returns a string."""
        obj = BaseModel()
        self.assertIsInstance(str(obj), str)

    def test_str_contains_class_name(self):
        """Test __str__ contains class name."""
        obj = BaseModel()
        self.assertIn("BaseModel", str(obj))


if __name__ == "__main__":
    unittest.main()
