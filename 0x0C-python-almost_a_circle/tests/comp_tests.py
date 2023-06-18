#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestProgram(unittest.TestCase):

    def test_base_init(self):
        self.e1 = Base()
        self.assertEqual(self.e1.id, 1)
        self.e2 = Base(34)
        self.assertEqual(self.e2.id, 34)
        self.e3 = Base()
        self.assertEqual(self.e3.id, 2)
        self.e4 = Base()
        self.assertEqual(self.e4.id, 3)
