#!/usr/bin/python3
"""
This module contains the BaseGeometry class.
"""


class BaseGeometry:
    """A class representing base geometry."""

    def area(self):
        """Raises an Exception indicating area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value to ensure it is an integer greater than 0.

        Args:
            name (str): The name parameter (always a string).
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
            """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
