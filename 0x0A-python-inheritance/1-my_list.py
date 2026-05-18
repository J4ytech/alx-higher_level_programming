#!/usr/bin/python3
"""
This module contains the MyList class.
"""


class MyList(list):
    """A subclass of the built-in list class."""

    def print_sorted(self):
        """Prints the elements of the list in ascending sorted order."""
        print(sorted(self))
