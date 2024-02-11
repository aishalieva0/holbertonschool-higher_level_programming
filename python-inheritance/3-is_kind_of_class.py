#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """
Check if an object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
     True if obj is an instance of a_class
        False, otherwise
    """
    return isinstance(obj, a_class)
