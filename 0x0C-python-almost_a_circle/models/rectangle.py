#!/usr/bin/python3
"""This module defines the Rectangle class that inherits from Base."""

from models.base import Base


class Rectangle(Base):
    """A class representing a rectangle, inheriting from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x coordinate. Defaults to 0.
            y (int): The y coordinate. Defaults to 0.
            id (int): The identity of the rectangle. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Prints in stdout the Rectangle instance with #, accounting for x and y"""
        for y in range(self.y):
            print()
        
        for row in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Returns the string representation of Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)
    
    def update(self, *args, **kwargs):
        """Update the Rectangle attributes using no-keyword arguments."""
        # If args exists and has at least 1 item
        if args and len(args) >= 1:
            self.id = args[0]
        
        # If args exists and has at least 2 items
        if args and len(args) >= 2:
            self.width = args[1]
            
        # If args exists and has at least 3 items
        if args and len(args) >= 3:
            self.height = args[2]
            
        # If args exists and has at least 4 items
        if args and len(args) >= 4:
            self.x = args[3]
            
        # If args exists and has at least 5 items
        if args and len(args) >= 5:
            self.y = args[4]
        
        #Otherwise, if args is empty, use the kwargs dictionary
        for key, value in kwargs.items():
            setattr(self, key, value)

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x coordinate."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x coordinate."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y coordinate."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y coordinate."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
