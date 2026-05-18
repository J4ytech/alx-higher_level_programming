#!/usr/bin/python3
"""
Module: 5-save_to_json_file
This module defines a function that writes
a Python object to a text file using JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using JSON representation.

    Args:
        my_obj: The Python object to serialize.
        filename (str): The path to the file.

    Returns:
        None
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
        f.write("\n")
