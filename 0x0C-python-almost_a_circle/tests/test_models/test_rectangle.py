#!/usr/bin/python3
"""This module test the Rectangle class with a multitude of tests.
"""
import unittest
from models.rectangle import Rectangle
import sys
from io import StringIO
import doctest
import models.rectangle


class Test_rectangle(unittest.TestCase):
    """This is the great amount of tests are located.
    """

    def test_rect_id(self):
        rec1 = Rectangle(30, 25)
        rec1_2 = Rectangle(40, 20)
        self.assertEqual(rec1.id, rec1_2.id - 1)

    def test_rect_id1(self):
        rec2 = Rectangle(40, 20, 4)
        rec2_2 = Rectangle(50, 34, 3)
        self.assertEqual(rec2.id, rec2_2.id - 1)

    def test_rect_id2(self):
        rec3 = Rectangle(50, 30, 3, 5)
        rec2_2 = Rectangle(37, 15, 2, 4)
        self.assertEqual(rec3.id, rec2_2.id - 1)

    def test_rect_id3(self):
        rec4 = Rectangle(35, 15, 2, 3, 17)
        self.assertEqual(rec4.id, 17)

    def test_rect_id4(self):
        rec5 = Rectangle(47, 24, 4, 6)
        rec5_2 = Rectangle(66, 22, 3, 7)
        self.assertEqual(rec5.id, rec5_2.id - 1)

    def test_rect_id5(self):
        rec6 = Rectangle(55, 33, 2, 4, -23)
        self.assertEqual(rec6.id, -23)

    def test_rect_id6(self):
        rec7 = Rectangle(70, 40, 3, 5, 0)
        self.assertEqual(rec7.id, 0)

    def test_rect_id7(self):
        rec7 = Rectangle(70, 40, 3, 5, "yeah")
        self.assertEqual(rec7.id, 'yeah')

    def test_rect_id8(self):
        rec7 = Rectangle(70, 40, 3, 5, [2, 3, 5, 6])
        self.assertEqual(rec7.id, [2, 3, 5, 6])

    def test_rect_area(self):
        rect1 = Rectangle(30, 25, 0, 0, 25)
        self.assertEqual(rect1.area(), 750)

    def test_rect_area1(self):
        rect2 = Rectangle(40, 20, 4, 0, 0)
        self.assertEqual(rect2.area(), 800)

    def test_rect_area2(self):
        rect3 = Rectangle(50, 30, 3, 5, -99)
        self.assertEqual(rect3.area(), 1500)

    def test_rect_str(self):
        r1 = Rectangle(50, 30, 0, 0, 35)
        self.assertEqual(str(r1), "[Rectangle] (35) 0/0 - 50/30")

    def test_rect_str1(self):
        r2 = Rectangle(30, 12, 3, 4, -71)
        self.assertEqual(str(r2), "[Rectangle] (-71) 3/4 - 30/12")

    def test_rect_str2(self):
        r3 = Rectangle(60, 35, 0, 0, 0)
        self.assertEqual(str(r3), "[Rectangle] (0) 0/0 - 60/35")

    def test_rect_str3(self):
        r3 = Rectangle(60, 35, 0, 0, "rizz")
        self.assertEqual(str(r3), "[Rectangle] (rizz) 0/0 - 60/35")

    def test_rect_str4(self):
        r3 = Rectangle(60, 35, 0, 0, [4, 5, 9])
        self.assertEqual(str(r3), "[Rectangle] ([4, 5, 9]) 0/0 - 60/35")

    @staticmethod
    def capt_out(ret):
        out = StringIO()
        dix = sys.stdout
        sys.stdout = out

        ret.display()

        sys.stdout = dix
        return out

    def test_rect_display(self):
        rg1 = Rectangle(6, 3, 0, 0, 1)

        b = self.capt_out(rg1)
        expected = "######\n######\n######\n"
        self.assertEqual(b.getvalue(), expected)

    def test_rect_display1(self):
        rg2 = Rectangle(4, 2, 0, 0, 1)

        x = self.capt_out(rg2)
        expected = "####\n####\n"
        self.assertEqual(x.getvalue(), expected)

    def test_rect_display2(self):
        rg3 = Rectangle(2, 4, 0, 0, 1)

        x = self.capt_out(rg3)
        expected = "##\n##\n##\n##\n"
        self.assertEqual(x.getvalue(), expected)

    def test_rect_display_han_x_y(self):
        qw = Rectangle(5, 3, 2, 3, 15)

        d = self.capt_out(qw)
        expected = "\n\n\n  #####\n  #####\n  #####\n"
        self.assertEqual(d.getvalue(), expected)

    def test_rect_display_han_x_y1(self):
        st = Rectangle(5, 2, 3, 0, -5)

        f = self.capt_out(st)
        expected = "   #####\n   #####\n"
        self.assertEqual(f.getvalue(), expected)

    def test_rect_display_han_x_y2(self):
        st = Rectangle(3, 5, 3, 0, -5)

        f = self.capt_out(st)
        expected = "   ###\n   ###\n   ###\n   ###\n   ###\n"
        self.assertEqual(f.getvalue(), expected)

    def test_rect_display_han_x_y3(self):
        st = Rectangle(3, 5, 0, 3, -5)

        f = self.capt_out(st)
        expected = "\n\n\n###\n###\n###\n###\n###\n"
        self.assertEqual(f.getvalue(), expected)

    def test_rect_update1(self):
        re1 = Rectangle(2, 2, 2, 2, 2)
        re1.update(14)
        self.assertEqual(str(re1), "[Rectangle] (14) 2/2 - 2/2")

    def test_rect_update2(self):
        re1 = Rectangle(2, 2, 2, 2, 2)
        re1.update(14, 30)
        self.assertEqual(str(re1), "[Rectangle] (14) 2/2 - 30/2")

    def test_rect_update3(self):
        re1 = Rectangle(2, 2, 2, 2, 2)
        re1.update(14, 30, 15)
        self.assertEqual(str(re1), "[Rectangle] (14) 2/2 - 30/15")

    def test_rect_update4(self):
        re1 = Rectangle(2, 2, 2, 2, 2)
        re1.update(14, 30, 15, 4)
        self.assertEqual(str(re1), "[Rectangle] (14) 4/2 - 30/15")

    def test_rect_update5(self):
        re1 = Rectangle(2, 2, 2, 2, 2)
        re1.update(14, 30, 15, 4, 7)
        self.assertEqual(str(re1), "[Rectangle] (14) 4/7 - 30/15")

    def test_rect_update5_7(self):
        re1 = Rectangle(2, 2, 2, 2, 2)
        re1.update('fly', 30, 15, 4, 7)
        self.assertEqual(str(re1), "[Rectangle] (fly) 4/7 - 30/15")

    def test_rect_update6(self):
        re1 = Rectangle(2, 2, 2, 2, 2)
        re1.update(width=50, height=35)
        self.assertEqual(str(re1), "[Rectangle] (2) 2/2 - 50/35")

    def test_rect_update7(self):
        re1 = Rectangle(2, 2, 2, 2, 2)
        re1.update(width=50, height=35, id=5)
        self.assertEqual(str(re1), "[Rectangle] (5) 2/2 - 50/35")

    def test_rect_update8(self):
        re1 = Rectangle(2, 2, 2, 2, 2)
        re1.update(x=3, width=50, height=35, id=27)
        self.assertEqual(str(re1), "[Rectangle] (27) 3/2 - 50/35")

    def test_rect_update9(self):
        re1 = Rectangle(2, 2, 2, 2, 2)
        re1.update(id=27, x=3, y=5, height=35, width=50)
        self.assertEqual(str(re1), "[Rectangle] (27) 3/5 - 50/35")

    def test_rect_update10(self):
        re1 = Rectangle(2, 2, 2, 2, 2)
        re1.update(id=[2, 9, 6], x=3, y=5, height=35, width=50)
        self.assertEqual(str(re1), "[Rectangle] ([2, 9, 6]) 3/5 - 50/35")

    def test_rect_to_dictionary(self):
        za = Rectangle(50, 20, 7, 9, -44)
        my_dict = {'x': 7, 'y': 9, 'id': -44, 'height': 20, 'width': 50}
        self.assertEqual(za.to_dictionary(), my_dict)

    def test_rect_to_dictionary1(self):
        za = Rectangle(30, 15, 2, 4, 0)
        my_dict = {'x': 2, 'y': 4, 'id': 0, 'height': 15, 'width': 30}
        self.assertEqual(za.to_dictionary(), my_dict)

    def test_rect_to_dictionary2(self):
        za = Rectangle(30, 15, 2, 4, "attain")
        my_dict = {'x': 2, 'y': 4, 'id': 'attain', 'height': 15, 'width': 30}
        self.assertEqual(za.to_dictionary(), my_dict)

    def test_rect_to_dictionary3(self):
        za = Rectangle(30, 15, 2, 4, [5, 3, 9])
        my_dict = {'x': 2, 'y': 4, 'id': [5, 3, 9], 'height': 15, 'width': 30}
        self.assertEqual(za.to_dictionary(), my_dict)

    def test_rect_TypeError(self):
        with self.assertRaises(TypeError):
            ice = Rectangle("rizz", 30, 3, 5, 1)

    def test_width_errormsg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("rizz", 30, 3, 5, 1)

    def test_rect_TypeError1(self):
        with self.assertRaises(TypeError):
            ice = Rectangle(40, "yonko", 6, 7, -2)

    def test_height_errormsg(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(40, "yonko", 6, 7, -2)

    def test_rect_TypeError2(self):
        with self.assertRaises(TypeError):
            ice = Rectangle(40, 20, "crypt", 7, -2)

    def test_x_errormsg(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(40, 20, "crypt", 7, -2)

    def test_rect_TypeError3(self):
        with self.assertRaises(TypeError):
            ice = Rectangle(40, 20, 6, "freak", -2)

    def test_y_errormsg(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(40, 20, 6, "freak", -2)

    def test_rect_TypeError4(self):
        with self.assertRaises(ValueError):
            ice = Rectangle(-5, 22, 4, 6, 9)

    def test_rect_TypeError5(self):
        with self.assertRaises(ValueError):
            ice = Rectangle(0, 22, 4, 6, 9)

    def test_width_val_errormsg(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-5, 22, 4, 6, 9)
            Rectangle(0, 22, 4, 6, 9)

    def test_rect_TypeError6(self):
        with self.assertRaises(ValueError):
            ice = Rectangle(44, -8, 4, 6, 9)

    def test_rect_TypeError7(self):
        with self.assertRaises(ValueError):
            ice = Rectangle(44, 0, 4, 6, 9)

    def test_height_val_errormsg(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(44, -8, 4, 6, 9)
            Rectangle(44, 0, 4, 6, 9)

    def test_rect_TypeError8(self):
        with self.assertRaises(ValueError):
            ice = Rectangle(44, 22, -12, 6, 9)

    def test_x_val_errormsg(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(44, 22, -12, 6, 9)

    def test_rect_TypeError9(self):
        with self.assertRaises(ValueError):
            ice = Rectangle(44, 22, 4, -31, 9)

    def test_y_val_errormsg(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(44, 22, 4, -31, 9)

    def test_rect_TypeError10(self):
        with self.assertRaises(ValueError):
            ice = Rectangle(-44, -22, -4, -31, -9)

    def test_rect_TypeError11(self):
        with self.assertRaises(TypeError):
            ice = Rectangle("stuff", "timeless", "things", "freak", -2)

    def test_rect_TypeError12(self):
        with self.assertRaises(TypeError):
            ice = Rectangle([3, 6, 7], [-1, 2, 4], [1, 23, 5], [2, 7, 8], -2)

    def test_rect_TypeError13(self):
        with self.assertRaises(TypeError):
            ice = Rectangle()

    def test_rect_module_doc(self):
        self.assertIsNotNone(models.rectangle.__doc__)
        self.assertGreater(len(models.rectangle.__doc__), 1)

    def test_rect_module_class_doc(self):
        self.assertIsNotNone(Rectangle.__doc__)
        self.assertGreater(len(Rectangle.__doc__), 1)

    def test_rect_module_class_func1_doc(self):
        self.assertIsNotNone(Rectangle.__init__.__doc__)
        self.assertGreater(len(Rectangle.__init__.__doc__), 1)

    def test_rect_module_class_func2_doc(self):
        self.assertIsNotNone(Rectangle.width.__doc__)
        self.assertGreater(len(Rectangle.width.__doc__), 1)

    def test_rect_module_class_func3_doc(self):
        self.assertIsNotNone(Rectangle.height.__doc__)
        self.assertGreater(len(Rectangle.height.__doc__), 1)

    def test_rect_module_class_func4_doc(self):
        self.assertIsNotNone(Rectangle.x.__doc__)
        self.assertGreater(len(Rectangle.x.__doc__), 1)

    def test_rect_module_class_func5_doc(self):
        self.assertIsNotNone(Rectangle.y.__doc__)
        self.assertGreater(len(Rectangle.y.__doc__), 1)

    def test_rect_module_class_func6_doc(self):
        self.assertIsNotNone(Rectangle.area.__doc__)
        self.assertGreater(len(Rectangle.area.__doc__), 1)

    def test_rect_module_class_func7_doc(self):
        self.assertIsNotNone(Rectangle.display.__doc__)
        self.assertGreater(len(Rectangle.display.__doc__), 1)

    def test_rect_module_class_func8_doc(self):
        self.assertIsNotNone(Rectangle.__str__.__doc__)
        self.assertGreater(len(Rectangle.__str__.__doc__), 1)

    def test_rect_module_class_func9_doc(self):
        self.assertIsNotNone(Rectangle.update.__doc__)
        self.assertGreater(len(Rectangle.update.__doc__), 1)

    def test_rect_module_class_func10_doc(self):
        self.assertIsNotNone(Rectangle.to_dictionary.__doc__)
        self.assertGreater(len(Rectangle.to_dictionary.__doc__), 1)
