#!/usr/bin/python3
"""
Module: 11-student
This module defines a Student class with attributes,
a method to return its dictionary representation,
and a method to reload its attributes from a dictionary.
"""


class Student:
    """
    Defines a student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns the dictionary description of the Student instance.

        Returns:
            dict: A dictionary representation of the student.
        """
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        with values from the given dictionary.

        Args:
            json (dict): A dictionary containing new attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
