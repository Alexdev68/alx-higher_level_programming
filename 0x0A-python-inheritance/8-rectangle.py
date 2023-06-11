#!/usr/bin/python3
base_geometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(base_geometry):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        base_geometry().integer_validator("width", self.__width)
        base_geometry().integer_validator("height", self.__height)
