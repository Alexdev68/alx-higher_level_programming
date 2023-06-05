#!/usr/bin/python3
"""This module houses a function that defines a rectangle.
"""


class Rectangle:
    """This class contains a variety of instance methods and a public class \
            attribute.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """This instance method initializes self.__width and \
                self.__height.

            Raises:
                TypeError: If self.__width is not of type int. \
                        If self.__height is not of type int.
                ValueError: If self.__width is less than zero. \
                        If self.__height is less than zero.
        """
        Rectangle.number_of_instances += 1
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
        """Thi(self) the self.__height and then sets it to value.

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
                rec += str(self.print_symbol)
            if i != self.__height - 1:
                rec += "\n"
        return rec

    def __str__(self):
        """This is the instance method used so a print statement can print out\
                 correct output.
        """
        return self.print_rectangle()

    def __repr__(self):
        """This method used to get desired output when the repr() \
                function is called.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """This method print a message when an instance of Rectangle is \
                deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """This method checks which rectangle is bigger or if they are equal.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_1.area() == rect_2.area():
            return rect_1
        if rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        cls.width = size
        cls.height = size

        return Rectangle(cls.width, cls.height)
