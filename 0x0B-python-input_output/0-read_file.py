#!/usr/bin/python3
"""
This module defines a function to read a UTF-8 text file and print its content.
"""

def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints it to stdout.

    Args:
        filename (str): The path to the file to read.
    """
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        print(content)
