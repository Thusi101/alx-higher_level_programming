#!/usr/bin/python3
"""Lookup module.
Defines an object attribute and returns a list of lookup function."""


def lookup(obj):
    """Return a list of an available object attributes
    and methods of the object."""
    return (dir(obj))
