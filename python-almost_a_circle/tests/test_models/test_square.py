#!/usr/bin/python3
""" test for Square"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_square_constructor_with_one_argument(self):
        square = Square(1)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

    def test_square_constructor_with_two_arguments(self):
        square = Square(1, 2)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 0)

    def test_square_constructor_with_three_arguments(self):
        square = Square(1, 2, 3)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_square_constructor_with_string_arguments(self):
        square_str1 = Square("1")
        self.assertEqual(square_str1.size, 1)
        self.assertEqual(square_str1.x, 0)
        self.assertEqual(square_str1.y, 0)

        square_str2 = Square(1, "2")
        self.assertEqual(square_str2.size, 1)
        self.assertEqual(square_str2.x, 2)
        self.assertEqual(square_str2.y, 0)

        square_str3 = Square(1, 2, "3")
        self.assertEqual(square_str3.size, 1)
        self.assertEqual(square_str3.x, 2)
        self.assertEqual(square_str3.y, 3)

    def test_square_constructor_with_four_arguments(self):
        square = Square(1, 2, 3, 4)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 4)

    def test_square_constructor_with_negative_arguments(self):
        square_neg1 = Square(-1)
        self.assertEqual(square_neg1.size, 1)
        self.assertEqual(square_neg1.x, 0)
        self.assertEqual(square_neg1.y, 0)

        square_neg2 = Square(1, -2)
        self.assertEqual(square_neg2.size, 1)
        self.assertEqual(square_neg2.x, 0)
        self.assertEqual(square_neg2.y, 0)

        square_neg3 = Square(1, 2, -3)
        self.assertEqual(square_neg3.size, 1)
        self.assertEqual(square_neg3.x, 2)
        self.assertEqual(square_neg3.y, 0)

    def test_square_constructor_with_zero_argument(self):
        square_zero = Square(0)
        self.assertEqual(square_zero.size, 0)
        self.assertEqual(square_zero.x, 0)
        self.assertEqual(square_zero.y, 0)

    def test_str(self):
        square = Square(4, 2, 3, 1)
        self.assertEqual(str(square), "[Square] (1) 2/3 - 4")

    def test_to_dictionary(self):
        s1 = Square(10, 2, 1, 9)
        s1_dictionary = s1.to_dictionary()
        expected = {'id': 9, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(s1_dictionary, expected)

        s1 = Square(1, 0, 0, 9)
        s1_dictionary = s1.to_dictionary()
        expected = {'id': 9, 'x': 0, 'size': 1, 'y': 0}
        self.assertEqual(s1_dictionary, expected)

        s1.update(5, 5, 5, 5)
        s1_dictionary = s1.to_dictionary()
        expected = {'id': 5, 'x': 5, 'size': 5, 'y': 5}
        self.assertEqual(s1_dictionary, expected)

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

    def test_getter(self):
        r1 = Square(5)
        self.assertEqual(r1.size, 5)

    def test_setter(self):
        r1 = Square(5)
        r1.size = 8
        self.assertEqual(r1.size, 8)

    def test_string(self):
        r1 = Square(3)

        with self.assertRaises(TypeError):
            r1.size = "Hi"

    def test_negative(self):
        r1 = Square(6)

        with self.assertRaises(ValueError):
            r1.size = -5

    def test_zero(self):
        r1 = Square(6)

        with self.assertRaises(ValueError):
            r1.size = 0

    def test_decimal(self):
        r1 = Square(6)

        with self.assertRaises(TypeError):
            r1.size = 1.5

    def test_tuple(self):
        r1 = Square(7)

        with self.assertRaises(TypeError):
            r1.size = (2, 8)

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
