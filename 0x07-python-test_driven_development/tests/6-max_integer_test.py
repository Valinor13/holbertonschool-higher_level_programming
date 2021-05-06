#!/usr/bin/python3
"""
A module containing unittest code

"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_of_ints(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([7, 7, 7]), 7)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, 0, 10, 100]), 100)

    def test_of_floats(self):
        self.assertEqual(max_integer([1.0, 2.0, 3.0, 4.0]), 4.0)
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)
        self.assertEqual(max_integer([4.1, 3.2, 2.3, 1.4]), 4.1)

    def test_of_letters(self):
        self.assertEqual(max_integer(['a', 'b', 'c', 'd']), 'd')
        self.assertEqual(max_integer(['d', 'c', 'b', 'a']), 'd')
        self.assertEqual(max_integer(['d', 'd', 'd', 'd']), 'd')

    def test_of_lists(self):
        self.assertEqual(max_integer([[1, 2, 3, 4], [2, 3, 4, 5]]), [2, 3, 4, 5])
        self.assertEqual(max_integer([[5, 4, 3, 2], [4, 3, 2, 1]]), [5, 4, 3, 2])
        self.assertEqual(max_integer([[5, 5, 5, 5], [5, 5, 5, 5]]), [5, 5, 5, 5])

    def test_of_none(self):
        self.assertEqual(max_integer(), None)

if __name__ == '__main__':
    unittest.main()
