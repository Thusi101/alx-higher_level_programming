#!/usr/bin/python3
"""MyList module.
Defines a class MyList that is an inherited list class
MyList and method that prints the sorted list."""


class MyList(list):
    """Implements Mylist class."""

    def print_sorted(self):
        """Prints sorted ascending list order."""
        print(sorted(self))
