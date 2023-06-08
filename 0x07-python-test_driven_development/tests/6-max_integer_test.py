#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max(self):
        self.lt = [2, 1, -6, 85, 100, -85]
        self.assertEqual(max_integer(self.lt), 100)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([-34, -57, -123, -110]), -34)
        self.assertEqual(max_integer([12.7, 12.6, 12.9, 12.2]), 12.9)
        self.assertEqual(max_integer([-21, 4.2, 6.3, -55]), 6.3)
        self.assertEqual(max_integer([25]), 25)
        self.assertEqual(max_integer([56, 9, 39, 222]), 222)

    def test_return_none(self):
        self.list = []
        self.assertIsNone(max_integer(self.list))
