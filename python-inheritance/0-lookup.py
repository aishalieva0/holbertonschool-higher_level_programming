#!/usr/bin/python3
"""
contains method lookup that return
list of available attributes and methods of an object
"""


def lookup(obj):
    """returns list of attributes and methods of an object"""
    return dir(obj)
