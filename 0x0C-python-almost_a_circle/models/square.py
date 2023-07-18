#!/usr/bin/python3
"""This module imports the base class named ``Rectangle`` and the class
in this module named ``Square`` inherits form it.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class inherits form ``Rectangle``.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """This method initializes the Square by passing it's args into the
        parent class.

        Args:
            size(int): First parameter
            x(int): Second parameter
            y(int): Third parameter
            id(int): Fourth parametert

        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """These properties gets the self.size and then sets the value of
        self.width and self.height to it.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to zero.

        Returns:
            The public instance attribute self.size.

        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """This is the __str__ method.

        Returns:
            str: [Square] (<id>) <x>/<y> - <size>

        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"

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
            self.size = args[1]

        if len(args) > 2:
            self.x = args[2]

        if len(args) > 3:
            self.y = args[3]

        if len(args) == 0 or args is None:
            keys = kwargs.keys()

            for key in keys:
                if key == "id":
                    self.id = kwargs[key]

                if key == "size":
                    self.size = kwargs[key]

                if key == "x":
                    self.x = kwargs[key]

                if key == "y":
                    self.y = kwargs[key]

    def to_dictionary(self):
        """This method create a dictionary of the parameters of this class
        ``Square``.

        Returns:
            dict: A dictonary of the parameters of the class.

        """
        my_dict = {}

        my_dict.update({'id': self.id})
        my_dict.update({'x': self.x})
        my_dict.update({'size': self.size})
        my_dict.update({'y': self.y})

        return my_dict
