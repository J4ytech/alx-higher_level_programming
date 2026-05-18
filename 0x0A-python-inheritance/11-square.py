#!/usr/bin/python3
"""
This module contains the Square class that inherits from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square class that inherits from Rectangle."""

    def __init__(self, size):
        """Initializes the square with a validated size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """Returns a string description of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
