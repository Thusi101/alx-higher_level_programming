#!/usr/bin/python3
"""Rectangle module.

Defines a class Rectangle that inherits from BaseGeometry.
Contains a class Rectangle that inherits from
BaseGeometry and some methods.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents the Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Checks and sets the default attributes of Rectangle class."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
