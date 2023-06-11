#!/usr/bin/python3
"""This module contains an empty class.
"""


class BaseGeometry:
    """This class contains a or some methods that serve different purposes.
    """
    def area(self):
        """This method doesn't calculate area.

        Raises:
            Exception: if area() is called.
        """
        raise Exception('area() is not implemented')
