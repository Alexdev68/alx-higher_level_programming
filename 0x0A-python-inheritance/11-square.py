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
        self.__size = size

        self.integer_validator("size", self.__size)

        super().__init__(self.__size, self.__size)

    def area(self):
        """This method returns the area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
