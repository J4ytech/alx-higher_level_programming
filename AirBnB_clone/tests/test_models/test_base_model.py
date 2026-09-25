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
        """Test id exists."""
        obj = BaseModel()
        self.assertIn("id", obj.__dict__)

    def test_id_is_string(self):
        """Test id is a string."""
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)

    def test_dates_exist(self):
        """Test created_at and updated_at exist."""
        obj = BaseModel()
        self.assertIn("created_at", obj.__dict__)
        self.assertIn("updated_at", obj.__dict__)

    def test_dates_are_datetime(self):
        """Test dates are datetime objects."""
        obj = BaseModel()
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_unique_ids(self):
        """Test each instance has a unique id."""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_save_updates_updated_at(self):
        """Test save updates updated_at."""
        obj = BaseModel()
        old_updated_at = obj.updated_at

        obj.save()

        self.assertNotEqual(old_updated_at, obj.updated_at)

    def test_to_dict_returns_dict(self):
        """Test to_dict returns a dictionary."""
        obj = BaseModel()
        self.assertIsInstance(obj.to_dict(), dict)

    def test_to_dict_contains_class(self):
        """Test __class__ key exists."""
        obj = BaseModel()
        obj_dict = obj.to_dict()

        self.assertIn("__class__", obj_dict)
        self.assertEqual(obj_dict["__class__"], "BaseModel")

    def test_to_dict_datetime_to_string(self):
        """Test datetime values become strings."""
        obj = BaseModel()
        obj_dict = obj.to_dict()

        self.assertIsInstance(obj_dict["created_at"], str)
        self.assertIsInstance(obj_dict["updated_at"], str)

    def test_str_returns_string(self):
        """Test __str__ output."""
        obj = BaseModel()
        self.assertIsInstance(str(obj), str)

    """
    TASK 4 TESTS
    """

    def test_create_from_dict(self):
        """Test recreation from dictionary."""
        obj1 = BaseModel()
        obj1.name = "John"
        obj1.age = 20

        obj_dict = obj1.to_dict()

        obj2 = BaseModel(**obj_dict)

        self.assertEqual(obj1.id, obj2.id)
        self.assertEqual(obj1.name, obj2.name)
        self.assertEqual(obj1.age, obj2.age)

    def test_recreated_dates_are_datetime(self):
        """Test recreated dates are datetime objects."""
        obj1 = BaseModel()

        obj_dict = obj1.to_dict()
        obj2 = BaseModel(**obj_dict)

        self.assertIsInstance(obj2.created_at, datetime)
        self.assertIsInstance(obj2.updated_at, datetime)

    def test_recreated_object_is_different(self):
        """Test recreated object is not same object."""
        obj1 = BaseModel()

        obj_dict = obj1.to_dict()
        obj2 = BaseModel(**obj_dict)

        self.assertIsNot(obj1, obj2)

    def test_kwargs_ignores_class(self):
        """Test __class__ is not added as attribute."""
        obj = BaseModel()
        obj_dict = obj.to_dict()

        new_obj = BaseModel(**obj_dict)

        self.assertFalse("__class__" in new_obj.__dict__)


if __name__ == "__main__":
    unittest.main()