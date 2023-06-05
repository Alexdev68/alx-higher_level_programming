#!/usr/bin/python3
"""This module houses a function that defines a rectangle.
"""


class Rectangle:
    """This is an empty class.
    """
    def __init__(self, width=0, height=0):
        """This instance method initializes self.__width and \
                self.__height.

            Raises:
                TypeError: If self.__width is not of type int. \
                        If self.__height is not of type int.
                ValueError: If self.__width is less than zero. \
                        If self.__height is less than zero.
        """
        self.__width = width
        self.__height = height

        if not isinstance(self.__width, int):
            raise TypeError('width must be an integer')
        if self.__width < 0:
            raise ValueError('width must be >= 0')
        if not isinstance(self.__height, int):
            raise TypeError('height must be an integer')
        if self.__height < 0:
            raise ValueError('height must be >= 0')

    @property
    def width(self):
        """This gets the self.__width and then sets it to value.

        Raises:
            TypeError: If self.__width is not of type int.
            ValueError: If self.__width is less than zero.
        """
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

        if not isinstance(self.__width, int):
            raise TypeError('width must be an integer')
        if self.__width < 0:
            raise ValueError('width must be >= 0')

    @property
    def height(self):
        """This gets the self.__height and then sets it to value.

        Raises:
            TypeError: If self.__height is not of type int.
            ValueError: If self.__height is less than zero.
        """
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

        if not isinstance(self.__height, int):
            raise TypeError('height must be an integer')
        if self.__height < 0:
            raise ValueError('height must be >= 0')

    def area(self):
        """This calculates and returns the area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """This calculates and returns the perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width * 2) + (self.__height * 2)

    def print_rectangle(self):
        """This returns a string contain the blueprints to print out the \
                rectangle.
        """
        rec = ''
        emp = ''
        if self.__width == 0 or self.__height == 0:
            return emp

        for i in range(self.__height):
            for j in range(self.__width):
                rec += "#"
            if i != self.__height - 1:
                rec += "\n"
        return rec

    def __str__(self):
        return self.print_rectangle()
