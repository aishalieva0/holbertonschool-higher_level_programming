#!/usr/bin/python3
"""
model that contains class Rectangle
which is inherits class Base
"""
from models.base import Base


class Rectangle(Base):
    """
    class inherits clas base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, param):
        self.isInteger(param, 'width')

        self.__width = param

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, param):
        self.isInteger(param, 'height')

        self.__height = param

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, param):
        self.isInteger(param, 'x')

        self.__x = param

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, param):
        self.isInteger(param, 'y')

        self.__y = param

    def isInteger(self, value, param):
        """ checks if param is int or not """
        if type(value) is not int:
            raise TypeError(param + ' must be an integer')

        if value <= 0 and param in ('width', 'height'):
            raise ValueError(param + ' must be > 0')

        if value < 0 and param in ('x', 'y'):
            raise ValueError(param + ' must be >= 0')

    def area(self):
        """ return area """
        return self.__width * self.__height
