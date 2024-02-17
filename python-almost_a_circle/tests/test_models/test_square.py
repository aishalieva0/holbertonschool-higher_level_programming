#!/usr/bin/python3
""" test for Square"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_str(self):
        square = Square(4, 2, 3, 1)
        self.assertEqual(str(square), "[Square] (1) 2/3 - 4")

    def test_to_dictionary(self):
        square = Square(10, 5, 5, 1)
        square_dict = square.to_dictionary()
        self.assertEqual(square_dict, {'id': 1, 'size': 10, 'x': 5, 'y': 5})

    def test_update(self):
        square = Square(1, 1, 1, 1)
        square.update(2, 3, 4, 5)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.width, 3)
        self.assertEqual(square.height, 3)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 5)

        square = Square(1, 1, 1, 1)
        square.update(89)
        self.assertEqual(square.id, 89)
        square.update(89, 1)
        self.assertEqual(square.width, 1)
        square.update(89, 1, 2)
        self.assertEqual(square.x, 2)
        square.update(89, 1, 2, 3)
        self.assertEqual(square.y, 3)

        square.update(**{'id': 89})
        self.assertEqual(square.id, 89)
        square.update(**{'id': 89, 'size': 1})
        self.assertEqual(square.width, 1)
        square.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(square.x, 2)
        square.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(square.y, 3)

    def test_create(self):
        square = Square.create(**{'id': 89})
        self.assertEqual(square.id, 89)
        square = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(square.width, 1)
        square = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(square.x, 2)
        square = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(square.y, 3)

    def test_none(self):
        r1 = Square(5)

        with self.assertRaises(TypeError):
            r1.size = None

    def test_empty(self):
        r1 = Square(7)

        with self.assertRaises(TypeError):
            r1.size = ''

    def test_save_to_file_with_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            data = file.read()
            self.assertEqual(data, "[]")

    def test_load_from_file_2(self):
        s1 = Square(5)
        s2 = Square(8, 2, 5)

        linput = [s1, s2]
        Square.save_to_file(linput)
        loutput = Square.load_from_file()

        for i in range(len(linput)):
            self.assertEqual(linput[i].__str__(), loutput[i].__str__())
