#!/usr/bin/python3
"""This module houses a class ``MagicClass`` and imports math for pi."""
import math
import dis


class MagicClass:
    """This is a magic class that perfoorms a magic calcultion."""

    def __init__(self, radius):
        """This method assigns zero to self._MagicClass__radius the radius

        Arg:
            radius(int or float): This is a value that can be either float or
             int

        Raises:
            TypeError: If the type of radius is not an int of float

        Returns:
            None
        """
        self._MagicClass__radius = 0

        if type(radius) is not int:
            if type(radius) is not float:
                raise TypeError('radius must be a number')
        self._MagicClass__radius = radius
        return None

    def area(self):
        """area method

        Returns:
            int: (self._MagicClass__radius ** 2) * math.pi)
        """
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """circumference method

        Returns:
            int: (2 * math.pi) * self._MagicClass__radius
        """
        return 2 * math.pi * self._MagicClass__radius


dis.dis(MagicClass)
