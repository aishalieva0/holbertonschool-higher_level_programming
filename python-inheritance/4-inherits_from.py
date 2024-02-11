#!/usr/bin/python3
"""
defines inherited class-checking function
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that
    inherited (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
    If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
