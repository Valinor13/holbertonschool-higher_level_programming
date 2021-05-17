#!/usr/bin/python3
"""A module that contains unit tests for the Rectangle class"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestRectClass(unittest.TestCase):
    """A class that stores tests for Rectangle"""

    def test_rectangle_exists(self):
        rect1 = Rectangle(1, 2)
        self.assertEqual(rect1.width, 1)
        self.assertEqual(rect1.height, 2)

    def test_rectangle_raises_errors(self):
        with self.assertRaises(TypeError):
            rect1 = Rectangle("1", 2)
        with self.assertRaises(TypeError):
            rect1 = Rectangle(1, "2")
        with self.assertRaises(TypeError):
            rect1 = Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            rect1 = Rectangle(1, 2, 3, "4")

    def test_rectangle_full_profile(self):
        rect1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rect1.width, 1)
        self.assertEqual(rect1.height, 2)
        self.assertEqual(rect1.x, 3)
        self.assertEqual(rect1.y, 4)
        self.assertEqual(rect1.id, 5)

if __name__ == '__main__':
        unittest.main()
