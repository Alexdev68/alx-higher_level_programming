#!/usr/bin/python3
"""This module import a class from 9-rectangle and the class defined here \
        inherits it.
"""
rectangle = __import__('9-rectangle').Rectangle


class Square(rectangle):
    """This class contains a method that validates it's args by inheriting \
            from the parent class.
    """
    def __init__(self, size):
        """This method inherits integer_validator to validate size.

        Arg:
            size(int): This is the size of the square
        """

        super().__init__(size, size)

        super().integer_validator("size", size)

        self.__size = size

    def area(self):
        """This method returns the area of the square.
        """
        return self.__size ** 2
