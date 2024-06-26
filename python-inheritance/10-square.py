#!/usr/bin/python3
"""
Contains parent class BaseGeometry
Contains subclass Rectangle
Contains subclass Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from Rectangle, who inherits from BaseGeometry
    methods:
        __init__(self, size)
    """
    def __init__(self, size):
        """initializes size
        Args:
            size (int): private
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
