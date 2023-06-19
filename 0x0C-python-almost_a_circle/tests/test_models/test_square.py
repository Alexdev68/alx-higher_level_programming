#!/usr/bin/python3
"""This module tests Square class with an multitude of tests.
"""
import unittest
from models.square import Square
import sys
from io import StringIO
import models.square


class Test_square(unittest.TestCase):
    """This class contains all the tests.
    """

    def test_sqr_id(self):
        sq1 = Square(30, 2)
        sq1_2 = Square(44, 27)
        self.assertEqual(sq1.id, sq1_2.id - 1)

    def test_sqr_id1(self):
        sq2 = Square(40, 20, 4)
        sq2_2 = Square(33, 11, 5)
        self.assertEqual(sq2.id, sq2_2.id - 1)

    def test_sqr_id2(self):
        sq3 = Square(50, 30, 3)
        sq3_2 = Square(55, 30, 2)
        self.assertEqual(sq3.id, sq3_2.id - 1)

    def test_sqr_id3(self):
        sq4 = Square(35, 15, 2, 17)
        self.assertEqual(sq4.id, 17)

    def test_sqr_id4(self):
        sq5 = Square(47, 24, 5)
        sq5_2 = Square(60, 3, 5)
        self.assertEqual(sq5.id, sq5_2.id - 1)

    def test_sqr_id5(self):
        sq6 = Square(55, 33, 2, -23)
        self.assertEqual(sq6.id, -23)

    def test_sqr_id6(self):
        sq7 = Square(70, 40, 3, 0)
        self.assertEqual(sq7.id, 0)

    def test_sqr_id7(self):
        sq7 = Square(70, 40, 3, "yeah")
        self.assertEqual(sq7.id, 'yeah')

    def test_sqr_id8(self):
        sq7 = Square(70, 40, 3, [2, 3, 5, 6])
        self.assertEqual(sq7.id, [2, 3, 5, 6])

    def test_sqr_area(self):
        sqr1 = Square(30, 25, 0, 0)
        self.assertEqual(sqr1.area(), 900)

    def test_sqr_area1(self):
        sqr2 = Square(40, 20, 4, 0)
        self.assertEqual(sqr2.area(), 1600)

    def test_sqr_area2(self):
        sqr3 = Square(50, 30, 3, -99)
        self.assertEqual(sqr3.area(), 2500)

    def test_sqr_str(self):
        r1 = Square(50, 0, 0, 35)
        self.assertEqual(str(r1), "[Square] (35) 0/0 - 50")

    def test_sqr_str1(self):
        r2 = Square(30, 3, 4, -71)
        self.assertEqual(str(r2), "[Square] (-71) 3/4 - 30")

    def test_sqr_str2(self):
        r3 = Square(60, 0, 0, 0)
        self.assertEqual(str(r3), "[Square] (0) 0/0 - 60")

    def test_sqr_str3(self):
        r3 = Square(60, 0, 0, "rizz")
        self.assertEqual(str(r3), "[Square] (rizz) 0/0 - 60")

    def test_sqr_str4(self):
        r3 = Square(60, 0, 0, [4, 5, 9])
        self.assertEqual(str(r3), "[Square] ([4, 5, 9]) 0/0 - 60")

    @staticmethod
    def capt_out(ret):
        out = StringIO()
        dix = sys.stdout
        sys.stdout = out

        ret.display()

        sys.stdout = dix
        return out

    def test_sqr_display(self):
        rg1 = Square(6, 0, 0, 1)

        b = self.capt_out(rg1)
        expected = "######\n######\n######\n######\n######\n######\n"
        self.assertEqual(b.getvalue(), expected)

    def test_sqr_display1(self):
        rg2 = Square(4, 0, 0, 1)

        x = self.capt_out(rg2)
        expected = "####\n####\n####\n####\n"
        self.assertEqual(x.getvalue(), expected)

    def test_sqr_display2(self):
        rg3 = Square(2, 0, 0, 1)

        x = self.capt_out(rg3)
        expected = "##\n##\n"
        self.assertEqual(x.getvalue(), expected)

    def test_sqr_display_han_x_y(self):
        qw = Square(5, 2, 3, 15)

        d = self.capt_out(qw)
        expected = "\n\n\n  #####\n  #####\n  #####\n  #####\n  #####\n"
        self.assertEqual(d.getvalue(), expected)

    def test_sqr_display_han_x_y1(self):
        st = Square(5, 3, 0, -5)

        f = self.capt_out(st)
        expected = "   #####\n   #####\n   #####\n   #####\n   #####\n"
        self.assertEqual(f.getvalue(), expected)

    def test_sqr_display_han_x_y2(self):
        st = Square(3, 3, 0, -5)

        f = self.capt_out(st)
        expected = "   ###\n   ###\n   ###\n"
        self.assertEqual(f.getvalue(), expected)

    def test_sqr_display_han_x_y3(self):
        st = Square(3, 0, 3, -5)

        f = self.capt_out(st)
        expected = "\n\n\n###\n###\n###\n"
        self.assertEqual(f.getvalue(), expected)

    def test_sqr_update1(self):
        re1 = Square(2, 2, 2, 2)
        re1.update(14)
        self.assertEqual(str(re1), "[Square] (14) 2/2 - 2")

    def test_sqr_update2(self):
        re1 = Square(2, 2, 2, 2)
        re1.update(14, 30)
        self.assertEqual(str(re1), "[Square] (14) 2/2 - 30")

    def test_sqr_update3(self):
        re1 = Square(2, 2, 2, 2)
        re1.update(14, 30, 4)
        self.assertEqual(str(re1), "[Square] (14) 4/2 - 30")

    def test_sqr_update4(self):
        re1 = Square(2, 2, 2, 2)
        re1.update(14, 30, 4, 7)
        self.assertEqual(str(re1), "[Square] (14) 4/7 - 30")

    def test_sqr_update5(self):
        re1 = Square(2, 2, 2, 2)
        re1.update(14, 30, 4, 7)
        self.assertEqual(str(re1), "[Square] (14) 4/7 - 30")

    def test_sqr_update5_7(self):
        re1 = Square(2, 2, 2, 2)
        re1.update('fly', 30, 4, 7)
        self.assertEqual(str(re1), "[Square] (fly) 4/7 - 30")

    def test_sqr_update6(self):
        re1 = Square(2, 2, 2, 2)
        re1.update(size=50)
        self.assertEqual(str(re1), "[Square] (2) 2/2 - 50")

    def test_sqr_update7(self):
        re1 = Square(2, 2, 2, 2)
        re1.update(size=50, id=5)
        self.assertEqual(str(re1), "[Square] (5) 2/2 - 50")

    def test_sqr_update8(self):
        re1 = Square(2, 2, 2, 2)
        re1.update(x=3, size=50, id=27)
        self.assertEqual(str(re1), "[Square] (27) 3/2 - 50")

    def test_sqr_update9(self):
        re1 = Square(2, 2, 2, 2)
        re1.update(id=27, x=3, y=5, size=50)
        self.assertEqual(str(re1), "[Square] (27) 3/5 - 50")

    def test_sqr_update10(self):
        re1 = Square(2, 2, 2, 2)
        re1.update(id=[2, 9, 6], x=3, y=5, size=50)
        self.assertEqual(str(re1), "[Square] ([2, 9, 6]) 3/5 - 50")

    def test_sqr_to_dictionary(self):
        za = Square(50, 7, 9, -44)
        my_dict = {'x': 7, 'y': 9, 'id': -44, 'size': 50}
        self.assertEqual(za.to_dictionary(), my_dict)

    def test_sqr_to_dictionary1(self):
        za = Square(30, 2, 4, 0)
        my_dict = {'x': 2, 'y': 4, 'id': 0, 'size': 30}
        self.assertEqual(za.to_dictionary(), my_dict)

    def test_sqr_to_dictionary2(self):
        za = Square(30, 2, 4, "attain")
        my_dict = {'x': 2, 'y': 4, 'id': 'attain', 'size': 30}
        self.assertEqual(za.to_dictionary(), my_dict)

    def test_sqr_to_dictionary3(self):
        za = Square(30, 2, 4, [5, 3, 9])
        my_dict = {'x': 2, 'y': 4, 'id': [5, 3, 9], 'size': 30}
        self.assertEqual(za.to_dictionary(), my_dict)

    def test_sqr_TypeError(self):
        with self.assertRaises(TypeError):
            ice = Square("rizz", 3, 5, 1)

    def test_sqr_TypeError1(self):
        with self.assertRaises(TypeError):
            ice = Square(40, "yonko", 7, -2)

    def test_sqr_TypeError2(self):
        with self.assertRaises(TypeError):
            ice = Square(40, 6, "crypt", -2)

    def test_sqr_TypeError4(self):
        with self.assertRaises(ValueError):
            ice = Square(-5, 4, 6, 9)

    def test_sqr_TypeError5(self):
        with self.assertRaises(ValueError):
            ice = Square(0, 4, 6, 9)

    def test_sqr_TypeError6(self):
        with self.assertRaises(ValueError):
            ice = Square(44, -8, 6, 9)

    def test_sqr_TypeError8(self):
        with self.assertRaises(ValueError):
            ice = Square(44, 2, -12, 9)

    def test_sqr_TypeError10(self):
        with self.assertRaises(ValueError):
            ice = Square(-44, -22, -4, -31)

    def test_sqr_TypeError11(self):
        with self.assertRaises(TypeError):
            ice = Square("stuff", "timeless", "things", "freak")

    def test_sqr_TypeError12(self):
        with self.assertRaises(TypeError):
            ice = Square([3, 6, 7], [-1, 2, 4], [1, 23, 5], [2, 7, 8])

    def test_sqr_TypeError13(self):
        with self.assertRaises(TypeError):
            ice = Square()

    def test_sqr_module_doc(self):
        self.assertIsNotNone(models.square.__doc__)
        self.assertGreater(len(models.square.__doc__), 1)

    def test_sqr_module_class_doc(self):
        self.assertIsNotNone(Square.__doc__)
        self.assertGreater(len(Square.__doc__), 1)

    def test_sqr_module_class_func1_doc(self):
        self.assertIsNotNone(Square.__init__.__doc__)
        self.assertGreater(len(Square.__init__.__doc__), 1)

    def test_sqr_module_class_func2_doc(self):
        self.assertIsNotNone(Square.width.__doc__)
        self.assertGreater(len(Square.width.__doc__), 1)

    def test_sqr_module_class_func3_doc(self):
        self.assertIsNotNone(Square.height.__doc__)
        self.assertGreater(len(Square.height.__doc__), 1)

    def test_sqr_module_class_func4_doc(self):
        self.assertIsNotNone(Square.x.__doc__)
        self.assertGreater(len(Square.x.__doc__), 1)

    def test_sqr_module_class_func5_doc(self):
        self.assertIsNotNone(Square.y.__doc__)
        self.assertGreater(len(Square.y.__doc__), 1)

    def test_sqr_module_class_func6_doc(self):
        self.assertIsNotNone(Square.area.__doc__)
        self.assertGreater(len(Square.area.__doc__), 1)

    def test_sqr_module_class_func7_doc(self):
        self.assertIsNotNone(Square.display.__doc__)
        self.assertGreater(len(Square.display.__doc__), 1)

    def test_sqr_module_class_func8_doc(self):
        self.assertIsNotNone(Square.__str__.__doc__)
        self.assertGreater(len(Square.__str__.__doc__), 1)

    def test_sqr_module_class_func9_doc(self):
        self.assertIsNotNone(Square.update.__doc__)
        self.assertGreater(len(Square.update.__doc__), 1)

    def test_sqr_module_class_func10_doc(self):
        self.assertIsNotNone(Square.to_dictionary.__doc__)
        self.assertGreater(len(Square.to_dictionary.__doc__), 1)
