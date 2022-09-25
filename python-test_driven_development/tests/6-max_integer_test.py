#!/usr/bin/python3
"""Interactive tests"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_notinteger(self):
        """test what happens when not integers are passed"""
        self.assertNotIsInstance(max_integer('B'), int)

    def test_max_at_end(self):
        """test when max integer at the end"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """test when max integer at the beginning"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_middle(self):
        """test when max is at the middle"""
        list = [1, 5, 80, 4, 7]
        self.assertEqual(max_integer(list), 80)

    def test_one_element(self):
        """when list is one element long"""
        list = [150]
        self.assertEqual(max_integer(list), 150)

    def test_empty(self):
        """test when list is empty"""
        list = []
        self.assertEqual(max_integer(list), None)
