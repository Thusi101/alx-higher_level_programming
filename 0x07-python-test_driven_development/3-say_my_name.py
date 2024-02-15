#!/usr/bin/python3
"""
This is the say_my_name module.

This module supplies one function, say_my_name().
"""


def say_my_name(first_name: str, last_name: str = "") -> None:
    """
    Print My name is <first name> <last name>.

    Args:
        first_name: The first name.
        last_name: The last name. (Optional)
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if not first_name:
        raise ValueError("first_name cannot be empty")

    full_name = first_name
    if last_name:
        full_name += " " + last_name

    print("My name is", full_name)
