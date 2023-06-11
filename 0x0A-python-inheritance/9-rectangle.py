#!/usr/bin/python3
"""This module import a class from 7-base_goemetry and the class defined here \
        inherits it.
"""
base_geometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(base_geometry):
    """This class contains a method that validates it's args by inheriting \
            from the parent class.
    """
    def __init__(self, width, height):
        """This method inherits integer_validator to validate width and height.
        """
        self.__width = width
        self.__height = height

        base_geometry().integer_validator("width", self.__width)
        base_geometry().integer_validator("height", self.__height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
