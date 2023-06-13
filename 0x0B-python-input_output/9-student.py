#!/usr/bin/python3
"""This module contains a class ``Student``.
"""


class Student:
    """This class retrieves a dictionary representation of a Student.
    """

    def __init__(self, first_name, last_name, age):
        """This method initializes some args.

        Args:
            first_name(str): This is the first name of the student.
            last_name(str): this is the last name of the student.
            age(int): This is the age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This method retrieves a dictionary representation of a Student.

        Returns:
            dict: a dictionary representation of a Student.
        """
        return vars(self)
