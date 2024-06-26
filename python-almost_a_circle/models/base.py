#!/usr/bin/python3
"""
model that contains class Base
"""
from os import path
import json
import turtle


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

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string to a file"""
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            j = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            file.write(j)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"

        if path.exists(filename) is False:
            return []

        with open(filename, mode='r', encoding='utf-8') as f:
            objs = cls.from_json_string(f.read())
            instances = []

            for el in objs:
                instances.append(cls.create(**el))

            return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        screen = turtle.Screen()
        screen.setup(width=600, height=600)
        screen.title("drawing rectangles and squares")

        pen = turtle.Turtle()

        for rectangle in list_rectangles:
            pen.penup()
            pen.goto(rectangle.x, rectangle.y)
            pen.pendown()
            pen.begin_fill()
            for _ in range(2):
                pen.forward(rectangle.width)
                pen.left(90)
                pen.forward(rectangle.height)
                pen.left(90)
            pen.end_fill()

        for square in list_squares:
            pen.penup()
            pen.goto(square.x, square.y)
            pen.pendown()
            pen.begin_fill()
            for _ in range(4):
                pen.forward(square.size)
                pen.left(90)
            pen.end_fill()

        screen.mainloop()
