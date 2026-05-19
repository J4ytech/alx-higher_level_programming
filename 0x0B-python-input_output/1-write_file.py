#!/usr/bin/python3
"""
Module: 1-write_file
This module defines a function to write a string to a UTF-8 text file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8) and returns
    the number of characters written.

    Args:
        filename (str): The path to the file.
        text (str): The string to write into the file.

    Returns:
        int: Number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
