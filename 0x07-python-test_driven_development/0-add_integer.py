#!/usr/bin/python3
"""
This is the add_integer module.

This module supplies one function, add_integer().
"""


def add_integer(a, b=98):
    """
    Return the addition of a and b.

    Args:
        a (int, float): the first value.
        b (int, float): the second value.
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer or float')
    
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer or float')

    return int(a) + int(b)
