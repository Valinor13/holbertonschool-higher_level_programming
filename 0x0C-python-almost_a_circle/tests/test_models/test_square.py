#!/usr/bin/python3
"""A module that contains unit tests for the Square class"""


import io
import os
import unittest
import unittest.mock
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectClass(unittest.TestCase):
    """A class that stores tests for Square"""

    def test_save_to_file_values(self):
        Square.save_to_file([Square(1)])
        self.assertTrue(os.path.exists("Square.json"))

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        self.assertTrue(os.path.exists("Square.json"))

    def test_save_to_file_empty(self):
        Square.save_to_file([])
        self.assertTrue(os.path.exists("Square.json"))

    def test_for_create(self):
        sqr1 = Square(3, 1, 2, 4)
        sqr1_dictionary = sqr1.to_dictionary()
        sqr2 = Square.create(**sqr1_dictionary)
        self.assertEqual(sqr2.size, 3)
        self.assertEqual(sqr2.x, 1)
        self.assertEqual(sqr2.y, 2)
        self.assertEqual(sqr2.id, 4)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_to_dictionary(self, mock_stdout):
        sqr1 = Square(5, 5, 5, 5)
        print(type(sqr1.to_dictionary()))
        self.assertEqual(mock_stdout.getvalue(), "<class 'dict'>\n")

    def test_of_update_empty(self):
        sqr1 = Square(5, 5, 5, 5)
        sqr1.update()
        self.assertEqual(sqr1.size, 5)
        self.assertEqual(sqr1.x, 5)
        self.assertEqual(sqr1.y, 5)
        self.assertEqual(sqr1.id, 5)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_of_display(self, mock_stdout):
        sqr1 = Square(1)
        sqr1.display()
        self.assertEqual(mock_stdout.getvalue(), "#\n")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_of_display_full(self, mock_stdout):
        sqr1 = Square(1, 1, 1)
        sqr1.display()
        self.assertEqual(mock_stdout.getvalue(), "\n #\n")

    def test_square_exists(self):
        sqr1 = Square(1)
        self.assertEqual(sqr1.size, 1)

    def test_square_type_errors(self):
        with self.assertRaises(TypeError):
            sqr1 = Square("1")
        with self.assertRaises(TypeError):
            sqr1 = Square(1, "3")
        with self.assertRaises(TypeError):
            sqr1 = Square(1, 3, "4")

    def test_square_value_errors(self):
        with self.assertRaises(ValueError):
            sqr1 = Square(-1)
        with self.assertRaises(ValueError):
            sqr1 = Square(0)
        with self.assertRaises(ValueError):
            sqr1 = Square(1, -3)
        with self.assertRaises(ValueError):
            sqr1 = Square(1, 3, -4)

    def test_str_exists(self):
        sqr1 = Square(4, 2, 1, 12)
        self.assertEqual(sqr1.__str__(), "[Square] (12) 2/1 - 4")

    def test_area_exists(self):
        sqr1 = Square(3)
        self.assertEqual(sqr1.area(), 9)

    def test_square_full_profile(self):
        sqr1 = Square(1, 2, 3, 4)
        self.assertEqual(sqr1.size, 1)
        self.assertEqual(sqr1.x, 2)
        self.assertEqual(sqr1.y, 3)
        self.assertEqual(sqr1.id, 4)

if __name__ == '__main__':
        unittest.main()
