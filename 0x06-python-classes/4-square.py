#!/usr/bin/python3
"""This module houses a class ``Square`` that defines a square.
"""


class Square:
    """This class defines a square.
    """

    def __init__(self, size=0):
        """__init__ method.

        Arg:
            size(int): Private instance attribute.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than zero.
        """
        self._Square__size = size

        if type(self._Square__size) != int:
            raise TypeError("size must be an integer")
        if self._Square__size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """Getter size method.

        Returns:
            int: The size of the square.

        Setter.

            Arg:
                value(int): This is the integer that the size is being set to.

            Raises:
                TypeError: if size is not an integer.
                ValueError: if size is less than zero.
        """
        return self._Square__size

    @size.setter
    def size(self, value):
        self._Square__size = value

        if type(self._Square__size) != int:
            raise TypeError("size must be an integer")
        if self._Square__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Area method.

        Returns:
            int: The result of size to the power of 2
        """
        return self._Square__size ** 2
