#!/usr/bin/python3
"""This module houses a function that defines a rectangle.
"""


class Rectangle:
    """This is an empty class.
    """
    def __init__(self, width=0, height=0):
        """This instance method initializes self._Rectangle__width and \
                self._Rectangle__height.

            Raises:
                TypeError: If self._Rectangle__width is not of type int. \
                        If self._Rectangle__height is not of type int.
                ValueError: If self._Rectangle__width is less than zero. \
                        If self._Rectangle__height is less than zero.
        """
        self._Rectangle__width = width
        self._Rectangle__height = height

        if not isinstance(self._Rectangle__width, int):
            raise TypeError('width must be an integer')
        if self._Rectangle__width < 0:
            raise ValueError('width must be >= 0')
        if not isinstance(self._Rectangle__height, int):
            raise TypeError('height must be an integer')
        if self._Rectangle__height < 0:
            raise ValueError('height must be >= 0')

    @property
    def width(self):
        """This gets the self._Rectangle__width and then sets it to value.

        Raises:
            TypeError: If self._Rectangle__width is not of type int.
            ValueError: If self._Rectangle__width is less than zero.
        """
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        self._Rectangle__width = value

        if not isinstance(self._Rectangle__width, int):
            raise TypeError('width must be an integer')
        if self._Rectangle__width < 0:
            raise ValueError('width must be >= 0')

    @property
    def height(self):
        """This gets the self._Rectangle__height and then sets it to value.

        Raises:
            TypeError: If self._Rectangle__height is not of type int.
            ValueError: If self._Rectangle__height is less than zero.
        """
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        self._Rectangle__height = value

        if not isinstance(self._Rectangle__height, int):
            raise TypeError('height must be an integer')
        if self._Rectangle__height < 0:
            raise ValueError('height must be >= 0')

    def area(self):
        return self._Rectangle__width * self._Rectangle__height

    def perimeter(self):
        if self._Rectangle__width == 0 or self._Rectangle__height == 0:
            return 0

        return (self._Rectangle__width * 2) + (self._Rectangle__height * 2)
