#!/usr/bin/python3
"""Module for testing Rectangle class"""
import unittest
from unittest.mock import patch 
import os
from io import StringIO
import sys
import contextlib
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Basic test for rectangle module"""
    def tearDown(self):
        Base._Base__nb_objects = 0
        self.assertEqual(Base._Base__nb_objects, 0)
    
    def test_valid(self):
        """fuction that test for good assignment of differents value"""
        r1 = Rectangle(10, 2, 34, 121, 45027310974)
        self.assertEqual(r1.id, 45027310974)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 34)
        self.assertEqual(r1.y, 121)
        r2 = Rectangle(1, 2)
        self.assertEqual(r2.id, 1)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 2)
        
    def test_wrong_values(self):
        """test wrong rectangles"""
        with self.assertRaises(TypeError):
            Rectangle("5", 5)
        with self.assertRaises(TypeError):
            Rectangle(5, "5")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError): 
            Rectangle(1, 2, 3, "4")
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(0, 5)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)
    
    def test_area(self):
        """test that area exists when
        right arguments provided"""

        r = Rectangle(3, 2).area()
        self.assertEqual(r, 6)

    def test_str(self):
        """Test if str representation is correct"""
        r = Rectangle(5, 6, 1, 2, 5)
        self.assertEqual(str(r), '[Rectangle] (5) 1/2 - 5/6')


    def test_create(self):
        """test that create is OK""" 
        rect_created = Rectangle.create(**{'id': 10, 'width': 5,
                                      'height': 10, 'x': 3, 'y': 4})
        answer = Rectangle(5, 10, 3, 4, 10)
        self.assertEqual(str(rect_created), str(answer))


    def test_update(self):
        """test that update function works
        and right args updated accordingly"""
        r = Rectangle(5, 6, 1, 2, 5)
        r_up = r.update(50, 60, 10, 20, 50)
        self.assertEqual(r.id, 50)
        self.assertEqual(r.width, 60)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 20)
        self.assertEqual(r.y, 50)

    def test_toDictionary(self):
        r1 = Rectangle(10, 10, 5, 0)
        self.assertTrue(type(r1.to_dictionary()), dict)
        self.assertEqual(r1.to_dictionary(), {
                         'id': 1, 'width': 10, 'height': 10, 'x': 5, 'y': 0})
    
if __name__ == "__main__":
    unittest.main()
    



