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

    def to_json(self, attrs=None):
        """This method retrieves a dictionary representation of a Student.

        Returns:
            dict: a dictionary representation of a Student based on the state \
                    of attrs.
        """
        if attrs is None:
            return vars(self)

        else:
            my_dict = {}
            for i in attrs:
                if i in ("first_name", "last_name", "age"):
                    val = getattr(self, i)
                    my_dict.update({i: val})

            return my_dict

    def reload_from_json(self, json):
        """This method sets the values of first name last name and age.
        """
        items = json.items()

        for name, val in items:
            if name == "first_name":
                self.first_name = val

            elif name == "last_name":
                self.last_name = val

            elif name == "age":
                self.age = val
