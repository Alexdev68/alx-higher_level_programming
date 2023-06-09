#!/usr/bin/python3
"""This module tests the Base class.
"""
import unittest
from os import remove
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_base(unittest.TestCase):
    """This class contains the tests.
    """

    def test_base_id(self):
        e1 = Base()
        e1_2 = Base()
        self.assertEqual(e1.id, e1_2.id - 1)

    def test_base_id1(self):
        e2 = Base(34)
        self.assertEqual(e2.id, 34)

    def test_base_id2(self):
        e3 = Base()
        e3_2 = Base()
        self.assertEqual(e3.id, e3_2.id - 1)

    def test_base_id3(self):
        e4 = Base()
        e4_2 = Base()
        self.assertEqual(e4.id, e4_2.id - 1)

    def test_base_id4(self):
        e5 = Base(-15)
        self.assertEqual(e5.id, -15)

    def test_base_id_list(self):
        e6 = Base([2, 5, 7, 9])
        self.assertEqual(e6.id, [2, 5, 7, 9])

    def test_base_id_string(self):
        e7 = Base("great")
        self.assertEqual(e7.id, 'great')

    def test_base_id_tuple(self):
        e8 = Base((2, 5, 3, 10))
        self.assertEqual(e8.id, (2, 5, 3, 10))

    def test_base_id_tuple(self):
        e9 = Base(2.6)
        self.assertEqual(e9.id, 2.6)

    def test_to_json_string(self):
        bas1 = Rectangle(40, 20, 4, 5, 1)
        dic = bas1.to_dictionary()
        json_dict = Base.to_json_string([dic])
        expected = '[{"x": 4, "y": 5, "id": 1, "height": 20, "width": 40}]'
        self.assertEqual(str(json_dict), expected)

    def test_to_json_string1(self):
        bas1 = Rectangle(20, 40, 4, 5, "pie")
        dic = bas1.to_dictionary()
        json_dict = Base.to_json_string([dic])
        expected = '[{"x": 4, "y": 5, "id": "pie", "height": 40, "width": 20}]'
        self.assertEqual(str(json_dict), expected)

    def test_to_json_string_none(self):
        bas2 = Base.to_json_string(None)
        self.assertEqual(str(bas2), '[]')

    def test_to_json_string_empty(self):
        bas3 = Base.to_json_string([])
        self.assertEqual(str(bas3), '[]')

    def test_to_json_string2(self):
        bas4 = Rectangle(20, 40, 4, 5, -3)
        bas4_2 = Rectangle(50, 30, 2, 3, 9).to_dictionary()
        dic = bas4.to_dictionary()
        json_dict = Base.to_json_string([dic, bas4_2])
        expected = '[{"x": 4, "y": 5, "id": -3, "height": 40, "width": 20}, '\
                   '{"x": 2, "y": 3, "id": 9, "height": 30, "width": 50}]'
        self.assertEqual(str(json_dict), expected)

    def test_to_json_string_square1(self):
        bas4 = Square(20, 4, 5, -3)
        bas4_2 = Square(50, 2, 3, 9).to_dictionary()
        dic = bas4.to_dictionary()
        json_dict = Base.to_json_string([dic, bas4_2])
        expected = '[{"id": -3, "x": 4, "size": 20, "y": 5}, '\
                   '{"id": 9, "x": 2, "size": 50, "y": 3}]'
        self.assertEqual(str(json_dict), expected)

    def test_to_json_string_square2(self):
        bas1 = Square(20, 4, 5, -3)
        dic = bas1.to_dictionary()
        json_dict = Base.to_json_string([dic])
        expected = '[{"id": -3, "x": 4, "size": 20, "y": 5}]'
        self.assertEqual(str(json_dict), expected)

    def test_save_to_file(self):
        r1 = Rectangle(33, 11, 5, 6, 1)
        Rectangle.save_to_file([r1])

        with open("Rectangle.json", 'r', encoding="UTF8")as f:
            data = f.read()

        self.assertEqual(len(data), 54)

    def test_save_to_file1(self):
        r2 = Rectangle(33, 11, 5, 6, 1)
        r2_2 = Rectangle(60, 44, 3, 5, 9)
        Rectangle.save_to_file([r2, r2_2])

        with open("Rectangle.json", 'r', encoding="UTF8")as f:
            data = f.read()

        self.assertEqual(len(data), 108)

    def test_save_to_file2(self):
        Rectangle.save_to_file(None)

        with open("Rectangle.json", 'r', encoding="UTF8")as f:
            data = f.read()

        self.assertEqual(len(data), 2)

    def test_save_to_file3(self):
        Rectangle.save_to_file([])

        with open("Rectangle.json", 'r', encoding="UTF8")as f:
            self.assertEqual(f.read(), '[]')

    def test_save_to_file_square1(self):
        s1 = Square(1, 2, 3, 4)
        Square.save_to_file([s1])
        with open("Square.json", 'r') as f:
            self.assertEqual(len(f.read()), 38)

    def test_save_to_file_square2(self):
        s1 = Square(1, 2, 3, 4)
        s2 = Square(4, 8, 12, 16)
        Square.save_to_file([s1, s2])
        with open("Square.json", 'r') as f:
            self.assertEqual(len(f.read()), 78)

    def test_save_to_file_square3(self):
        Square.save_to_file(None)

        with open("Square.json", 'r', encoding="UTF8")as f:
            data = f.read()

        self.assertEqual(len(data), 2)

    def test_save_to_file_square4(self):
        Square.save_to_file([])

        with open("Square.json", 'r', encoding="UTF8")as f:
            self.assertEqual(f.read(), '[]')

    def test_from_json_string(self):
        decoded = Base.from_json_string(None)

        self.assertEqual(decoded, [])

    def test_from_json_string1(self):
        decoded = Base.from_json_string("[]")

        self.assertEqual(decoded, [])

    def test_from_json_string(self):
        decoded = Base.from_json_string('[{"id": 95}]')

        self.assertEqual(decoded, [{'id': 95}])

    def test_create(self):
        mi_dict = {'id': 95}

        rit = Rectangle.create(**mi_dict)
        self.assertEqual(str(rit), "[Rectangle] (95) 0/0 - 5/7")

    def test_create(self):
        mi_dict = {'id': 95}

        rit = Square.create(**mi_dict)
        self.assertEqual(str(rit), "[Square] (95) 0/0 - 6")

    def test_load_from_file_square1(self):
        s1 = Square(1, 2, 3, 4)
        s2 = Square(3, 5, 7, 8)
        Square.save_to_file([s1, s2])
        mit = Square.load_from_file()
        self.assertEqual(len(mit), 2)

    def test_load_from_file_rectangle1(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(3, 5, 7, 8)
        Rectangle.save_to_file([r1, r2])
        mit = Rectangle.load_from_file()
        self.assertEqual(len(mit), 2)

    def test_load_from_file_square1_not_exists(self):
        try:
            remove("Square.json")
        except IOError:
            pass
        mit = Square.load_from_file()
        self.assertEqual(len(mit), 0)

    def test_load_from_file_rectangle1_not_exists(self):
        try:
            remove("Rectangle.json")
        except IOError:
            pass
        fit = Rectangle.load_from_file()
        self.assertEqual(len(fit), 0)
