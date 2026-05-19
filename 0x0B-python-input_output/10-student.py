#!/usr/bin/python3
"""
Module: 10-student
This module defines a Student class with attributes
and a method to return its dictionary representation,
optionally filtered by a list of attribute names.
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

    def to_json(self, attrs=None):
        """
        Returns the dictionary description of the Student instance.
        If attrs is a list of strings, only attributes with names
        in this list are returned.

        Args:
            attrs (list, optional): List of attribute names to retrieve.

        Returns:
            dict: A dictionary representation of the student.
        """
        if attrs is None:
            return self.__dict__
        return {key: self.__dict__[key] for key in attrs if key in self.__dict__}
