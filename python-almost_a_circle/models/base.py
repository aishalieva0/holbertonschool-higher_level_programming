#!/usr/bin/python3
"""
model that contains class Base
"""
import json


class Base:
    """
    defines class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns json """
        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
