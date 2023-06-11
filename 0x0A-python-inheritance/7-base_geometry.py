#!/usr/bin/python3
"""This module contains a class ``BaseGeometry``.
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

    def integer_validator(self, name, value):
        #self.__name = name
        #self.__value = value
        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
