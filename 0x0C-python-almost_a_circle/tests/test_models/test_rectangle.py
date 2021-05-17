#!/usr/bin/python3
"""A module that contains unit tests for the Rectangle class"""


import io
import os
import unittest
import unittest.mock
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectClass(unittest.TestCase):
    """A class that stores tests for Rectangle"""

    def test_save_to_file_values(self):
        Rectangle.save_to_file([Rectangle(1, 2)])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_save_to_file_empty(self):
        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_for_create(self):
        rect1 = Rectangle(3, 5, 1, 2, 4)
        rect1_dictionary = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dictionary)
        self.assertEqual(rect2.width, 3)
        self.assertEqual(rect2.height, 5)
        self.assertEqual(rect2.x, 1)
        self.assertEqual(rect2.y, 2)
        self.assertEqual(rect2.id, 4)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_to_dictionary(self, mock_stdout):
        rect1 = Rectangle(5, 5, 5, 5, 5)
        print(type(rect1.to_dictionary()))
        self.assertEqual(mock_stdout.getvalue(), "<class 'dict'>\n")

    def test_of_update_empty(self):
        rect1 = Rectangle(5, 5, 5, 5, 5)
        rect1.update()
        self.assertEqual(rect1.width, 5)
        self.assertEqual(rect1.height, 5)
        self.assertEqual(rect1.x, 5)
        self.assertEqual(rect1.y, 5)
        self.assertEqual(rect1.id, 5)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_of_display(self, mock_stdout):
        rect1 = Rectangle(1, 1)
        rect1.display()
        self.assertEqual(mock_stdout.getvalue(), "#\n")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_of_display_full(self, mock_stdout):
        rect1 = Rectangle(1, 1, 1, 1)
        rect1.display()
        self.assertEqual(mock_stdout.getvalue(), "\n #\n")

    def test_rectangle_exists(self):
        rect1 = Rectangle(1, 2)
        self.assertEqual(rect1.width, 1)
        self.assertEqual(rect1.height, 2)

    def test_rectangle_type_errors(self):
        with self.assertRaises(TypeError):
            rect1 = Rectangle("1", 2)
        with self.assertRaises(TypeError):
            rect1 = Rectangle(1, "2")
        with self.assertRaises(TypeError):
            rect1 = Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            rect1 = Rectangle(1, 2, 3, "4")

    def test_rectangle_value_errors(self):
        with self.assertRaises(ValueError):
            rect1 = Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            rect1 = Rectangle(1, -2)
        with self.assertRaises(ValueError):
            rect1 = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            rect1 = Rectangle(1, 0)
        with self.assertRaises(ValueError):
            rect1 = Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            rect1 = Rectangle(1, 2, 3, -4)

    def test_str_exists(self):
        rect1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(rect1.__str__(), "[Rectangle] (12) 2/1 - 4/6")

    def test_area_exists(self):
        rect1 = Rectangle(3, 4)
        self.assertEqual(rect1.area(), 12)

    def test_rectangle_full_profile(self):
        rect1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rect1.width, 1)
        self.assertEqual(rect1.height, 2)
        self.assertEqual(rect1.x, 3)
        self.assertEqual(rect1.y, 4)
        self.assertEqual(rect1.id, 5)

if __name__ == '__main__':
        unittest.main()
