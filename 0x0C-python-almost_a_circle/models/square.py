#!/usr/bin/python3
"""Defines the Square class that inherits from Rectangle."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class, a special case of Rectangle where width == height."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square (both width and height).
            x (int): The horizontal offset (default 0).
            y (int): The vertical offset (default 0).
            id (int): The identifier of the square (optional).
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the string representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
