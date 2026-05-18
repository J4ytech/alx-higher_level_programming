#!/usr/bin/python3
"""
Module: 4-from_json_string
This module defines a function that converts
a JSON string into a Python object.
"""

import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure)
    represented by a JSON string.

    Args:
        my_str (str): The JSON string to deserialize.

    Returns:
        object: The corresponding Python data structure.
    """
    return json.loads(my_str)
