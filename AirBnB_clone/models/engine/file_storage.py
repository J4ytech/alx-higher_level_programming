#!/usr/bin/python3
"""Defines the FileStorage class."""

import json


class FileStorage:
    """Serializes instances to a JSON file and
    deserializes JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        obj_dict = {}

        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            from models.base_model import BaseModel

            with open(FileStorage.__file_path, "r") as f:
                obj_dict = json.load(f)

                FileStorage.__objects = {}
                for key, value in obj_dict.items():
                    FileStorage.__objects[key] = BaseModel(**value)

        except FileNotFoundError:
            pass