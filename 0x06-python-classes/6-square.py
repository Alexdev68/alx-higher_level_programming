#!/usr/bin/python3
"""This module houses a class ``Square`` that defines a square.
"""


class Square:
    """This class defines a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """__init__ method.

        Arg:
            size(int): Private instance attribute.
            position(tuple): Private instance attribute.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than zero.
        """
        self._Square__size = size
        self.__position = position

        if type(self.__position) != tuple or len(self.__position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(self.__position[0]) != int or type(self.__position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if self.__position[0] < 0 or self.__position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

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

    @property
    def position(self):
        """Getter

        Returns:
            tuple: The self.__position

        Setter.

            Arg:
                value(tuple): This is what position is to be set to.

            Raises:
                TypeError: If position is not a tuple or if the size is not 2
                or if it's values aren't positive integers
        """
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

        if type(self.__position) != tuple or len(self.__position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(self.__position[0]) != int or type(self.__position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if self.__position[0] < 0 or self.__position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Area method.

        Returns:
            int: The result of size to the power of 2
        """
        return self._Square__size ** 2

    def my_print(self):
        """This prints a square with the ``#`` character and puts spaces using
         position.
        """
        if self._Square__size == 0:
            print("")
            return

        else:
            for ui in range(self.__position[1]):
                print()
            for i in range(self._Square__size):
                for j in range(self._Square__size):
                    if j == 0:
                        for h in range(self.__position[0]):
                            print(" ", end='')
                    print("#", end='')
                print()
