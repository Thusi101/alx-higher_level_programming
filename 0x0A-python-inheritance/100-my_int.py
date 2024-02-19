#!/usr/bin/python3
"""MyInt module.

Contains a class MyInt that inherits from int.
Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Defines the MyInt Class"""

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
