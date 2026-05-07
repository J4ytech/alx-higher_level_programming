#!/usr/bin/python3
"""
This module provides a function that prints a square using '#' characters.
It includes validation for size and type.
"""


def print_square(size):
    """
    Prints a square with the character # based on the size provided.
        
    Args:
        size (int): The height and width of the square.
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        for col in range(size):
            print("#", end="")
        print()
