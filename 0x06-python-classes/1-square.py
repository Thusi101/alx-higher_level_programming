#!/usr/bin/python3

"""Define a class Square.
This module contains a class that defines a square and init method that
sets its size.
"""

class Square:
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
