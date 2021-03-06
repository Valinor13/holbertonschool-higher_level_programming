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
        self.assertEqual(b1.id, 1)
        b2 = Base(None)
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_id_match(self):
        b1 = Base(1)
        self.assertEqual(b1.id, 1)
        b2 = Base(89)
        self.assertEqual(b2.id, 89)

    def test_to_json_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_empty_string(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_from_json_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_empty_string(self):
        self.assertEqual(Base.from_json_string(""), [])

if __name__ == '__main__':
    unittest.main()
