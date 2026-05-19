#!/usr/bin/python3
"""
Module: 2-append_write
This module defines a function to append a string to a UTF-8 text file.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF-8)
    and returns the number of characters added.

    Args:
        filename (str): The path to the file.
        text (str): The string to append.

    Returns:
        int: Number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
