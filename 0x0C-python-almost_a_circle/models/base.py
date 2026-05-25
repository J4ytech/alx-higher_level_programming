#!/usr/bin/python3
"""Defines the Base class for all models."""

import json


class Base:
    """Base class to manage id attribute for all future classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance with an optional id."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
