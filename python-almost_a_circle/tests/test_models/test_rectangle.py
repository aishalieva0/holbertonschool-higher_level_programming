#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_constructor(self):
        rect = Rectangle(10, 20)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertIsNotNone(rect.id)

    def test_area(self):
        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)

    def test_display(self):
        rect = Rectangle(3, 2)
        self.assertEqual(rect.display(), None)  # Assuming display just prints, returns None

    def test_str(self):
        rect = Rectangle(4, 8, 2, 3, 1)
        self.assertEqual(str(rect), "[Rectangle] (1) 2/3 - 4/8")

    def test_update(self):
        rect = Rectangle(1, 1, 0, 0, 1)
        rect.update(2, 3, 4, 5, 6)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 4)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 6)

    def test_to_dictionary(self):
        rect = Rectangle(10, 20, 5, 5, 1)
        rect_dict = rect.to_dictionary()
        self.assertEqual(rect_dict, {'id': 1, 'width': 10, 'height': 20, 'x': 5, 'y': 5})
