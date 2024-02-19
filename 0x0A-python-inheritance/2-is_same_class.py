#!/usr/bin/python3
"""MyList class-checking module .

defines a class-checking MyList that inherits from list
and a method that prints the sorted list.
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance
    of the specified class ; otherwise False.
    """
    return type(obj) is a_class
