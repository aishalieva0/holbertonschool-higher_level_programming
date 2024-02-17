#!/usr/bin/python3
"""
inherits class Base
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ ...  """
        str_square = "[Square]" 
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_size = "{}".format(self.width)
        return str_square + str_id + str_xy + str_size

