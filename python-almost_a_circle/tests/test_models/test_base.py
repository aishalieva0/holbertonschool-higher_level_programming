#!/usr/bin/python3
"""
test for Base class
"""
import unittest
import os
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle



class TestBase(unittest.TestCase):
    """
    class to test class Base
    """
    def setUp(self):
        """ test """
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_auto_assign_id(self):
        """  test assign id """
        base1 = Base()
        base2 = Base()
        base3 = Base()

        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 3)

    def test_to_json_string(self):
        """ test """
        rect = Rectangle(2, 4)
        rect.id = 1
        json_str = Base.to_json_string([rect.to_dictionary()])
        self.assertEqual(json_str, '[{"id": 1, "width": 2, "height": 4}]')

    def test_save_to_file(self):
        rect = Rectangle(2, 4)
        Base.save_to_file([rect])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_from_json_string(self):
        json_str = '[{"id": 1, "width": 2, "height": 4}]'
        rect_dicts = Base.from_json_string(json_str)
        self.assertEqual(rect_dicts, [{"id": 1, "width": 2, "height": 4}])

    def test_create(self):
        rect_dict = {"width": 3, "height": 5}
        rect = Rectangle.create(**rect_dict)
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 5)

    def test_load_from_file(self):
        rect = Rectangle(2, 4)
        Square.save_to_file([rect])
        instances = Square.load_from_file()
        self.assertEqual(len(instances), 1)
        self.assertEqual(instances[0].width, 2)
        self.assertEqual(instances[0].height, 4)
