#!/usr/bin/python3
"""
test for Base class
"""
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle



class TestBase(unittest.TestCase):
    """
    class to test class Base
    """
    def test_auto_assign_id(self):
        base1 = Base()
        base2 = Base()
        base3 = Base()

        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 3)
