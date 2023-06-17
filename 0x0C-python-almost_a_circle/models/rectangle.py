#!/usr/bin/python3
"""This module imports a base class named ``Base`` and the class contained
 in this module named ``Rectangle``, inherits from the imported ``Base`` class.
"""
from models.base import Base


class Rectangle(Base):
    """This class inherits from a class named ``Base``.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """This method passess it's id into the init of ``Base`` and then
         initialises all it's other args to private instance attributes.

        Args:
            width(int): This first parameter.
            height(int): This is the second parameter.
            x(int): This is the third parameter.
            y(int): This is the fourth parameter.

        Raises:
            TypeError: If any of the parameters (id excluded) is not an int.
            ValueError: If width or height is less than or equal to zero.
                        If x or y is less than zero.

        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        if not isinstance(self.__width, int):
            raise TypeError('width must be an integer')
        if not isinstance(self.__height, int):
            raise TypeError('height must be an integer')
        if not isinstance(self.__x, int):
            raise TypeError('x must be an integer')
        if not isinstance(self.__y, int):
            raise TypeError('y must be an integer')
        if self.__width <= 0:
            raise ValueError('width must be > 0')
        if self.__height <= 0:
            raise ValueError('height must be > 0')
        if self.__x < 0:
            raise ValueError('x must be >= 0')
        if self.__y < 0:
            raise ValueError('y must be >= 0')

    @property
    def width(self):
        """These properties gets the self.__width and then sets it's value to
         value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to zero.

        Returns:
            The private instance attribute self.__width.

        """
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

        if not isinstance(self.__width, int):
            raise TypeError('width must be an integer')
        if self.__width <= 0:
            raise ValueError('width must be > 0')

    @property
    def height(self):
        """These properties gets the self.__height and then sets it's value to
         value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to zero.

        Returns:
            The private instance attribute self.__height.

        """
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

        if not isinstance(self.__height, int):
            raise TypeError('height must be an integer')
        if self.__height <= 0:
            raise ValueError('height must be > 0')

    @property
    def x(self):
        """These properties gets the self.__x and then sets it's value to
         value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than zero.

        Returns:
            The private instance attribute self.__x.

        """
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

        if not isinstance(self.__x, int):
            raise TypeError('x must be an integer')
        if self.__x < 0:
            raise ValueError('x must be >= 0')

    @property
    def y(self):
        """These properties gets the self.__y and then sets it's value to
        value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than zero.

        Returns:
            The private instance attribute self.__y.

        """
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

        if not isinstance(self.__y, int):
            raise TypeError('y must be an integer')
        if self.__y < 0:
            raise ValueError('y must be >= 0')

    def area(self):
        """This method calculates the are of the rectangle.

        Returns:
            int: This multiplication of ``self.__width`` and ``self.height``.

        """
        return self.__width * self.__height

    def display(self):
        """This method print out the rectangle with the ``#`` character.
        """
        for h in range(self.__y):
            print()
        for i in range(self.__height):
            for b in range(self.__x):
                print(" ", end='')
            for j in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """This is the __str__ method.

        Returns:
            str: [Rectangle] (<id>) <x>/<y> - <width>/<height>.
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - "\
               f"{self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """This method assigns values to the parameters of this class
        from ``*args`` or ``**kwargs``.

        Args:
            *args(tuple): First parameter.
            **kwargs(dict): Second parameter.

        """
        if len(args) > 0:
            self.id = args[0]

        if len(args) > 1:
            self.width = args[1]

        if len(args) > 2:
            self.height = args[2]

        if len(args) > 3:
            self.x = args[3]

        if len(args) > 4:
            self.y = args[4]

        if len(args) == 0 or args is None:
            keys = kwargs.keys()

            for key in keys:
                if key == "id":
                    self.id = kwargs[key]

                if key == "width":
                    self.width = kwargs[key]

                if key == "height":
                    self.height = kwargs[key]

                if key == "x":
                    self.x = kwargs[key]

                if key == "y":
                    self.y = kwargs[key]

    def to_dictionary(self):
        """This method create a dictionary of the parameters of this class
        ``Rectangle``.

        Returns:
            dict: A dictonary of the parameters of the class.

        """
        my_dict = {}

        my_dict.update({'x': self.x})
        my_dict.update({'y': self.y})
        my_dict.update({'id': self.id})
        my_dict.update({'height': self.height})
        my_dict.update({'width': self.width})

        return my_dict
