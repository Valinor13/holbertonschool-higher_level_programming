#!/usr/bin/python3
"""A module that contains unit tests for the Rectangle class"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestRectClass(unittest.TestCase):
    """A class that stores tests for Rectangle"""

    def test_rectangle_exists(self):
        """A module that contains unit tests for the Base class"""

        rect1 = Rectangle(1, 2)
        self.assertIsInstance(rect1, Rectangle)

if __name__ == '__main__':
        unittest.main()
