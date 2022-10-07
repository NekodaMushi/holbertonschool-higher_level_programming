#!/usr/bin/python3
"""unittests stuff to test the stuff
I'm really understanding nothing at all
"""
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """class for testing Base class"""

    def tearDown(self):
        Base._Base__nb_objects = 0
        self.assertEqual(Base._Base__nb_objects, 0)

    def test_id(self):
        """Test that ID associated exists and match
        with new instances created"""
        b1 = Base()
        b2 = Base(523)
        b3 = Base(62)
        b4 = Base()
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 523)
        self.assertEqual(b3.id, 62)
        self.assertEqual(b4.id, 2)
        self.assertEqual(b5.id, 3)

    def test_type(self):
        """test type and instance"""
        b = Base()
        self.assertTrue(isinstance(b, Base))
        self.assertEqual(type(b), Base)

    def test_to_json_str_empty(self):
        """test if empty list produce what expected"""
        bjson = Base.to_json_string([])
        self.assertEqual(bjson, '[]')
    def test_to_json_content(self):
        """test if list of dict is converted to JSON content"""
        bjson = Base.to_json_string({"banjo": 500, "cithare":2560})
        self.assertTrue(type(bjson), str)
        self.assertEqual(bjson, '{"banjo": 500, "cithare": 2560}')
    def test_from_json_str(self):
        """test if JSON is converted to list
        case empty, None, and correct JSON provided"""
        blist = Base.from_json_string('[]')
        blist_1 = Base.from_json_string(None)
        blist_2 = Base.from_json_string('[{"Peach": 2.70, "Orange": 1.60}]')
        self.assertEqual(blist, [])
        self.assertEqual(blist_1, [])
        self.assertEqual(blist_2, [{'Peach': 2.7, 'Orange': 1.6}])
        self.assertTrue(type(blist), list)
        self.assertTrue(type(blist_2), list)

if __name__ == "__main__":
    unittest.main()
