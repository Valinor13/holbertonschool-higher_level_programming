#!/usr/bin/python3
"""A module that contains unit tests for the Base class"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """A class that stores tests for Base"""

    def test_auto_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(89)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 89)

if __name__ == '__main__':
    unittest.main()
