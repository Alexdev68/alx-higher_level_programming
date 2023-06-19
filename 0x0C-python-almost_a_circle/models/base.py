#!/usr/bin/python3
"""This module contains a class named ``Base``.
"""
import json
import csv
from turtle import *


class Base:
    """This class has a private class attribute named ``__nb_objects``.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """This method initializes id and assigns it to a public instance
        attribute named self.id if it's not None else it increments
        ``__nb_objects`` and assigns the value of ``__nb_objects`` to self.id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """This method changes a list of dictionaries to JSON string
        representation.

        Returns:
            str: "[]" if list_dictionaries is empty or non-existent else it
                 returns the JSON string representation of list_dictionaries.

        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """This method saves a list of dictionaries to a file.
        """
        dlist = []
        if not (list_objs is None or len(list_objs) == 0):
            for i in list_objs:
                dlist.append(i.to_dictionary())

        with open(cls.__name__ + '.json', 'w', encoding="UTF8") as f:
            f.write(cls.to_json_string(dlist))

    @staticmethod
    def from_json_string(json_string):
        """This method decodes a json string.

        Returns:
            list: [] if json_string is empty or non-existent else it returns
                  the decoded json string which is a list

        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """This creats an instanc with all attributes already set.

        Returns:
            instance: dumz.

        """
        if cls.__name__ == "Rectangle":
            dumz = cls(5, 7)
        elif cls.__name__ == "Square":
            dumz = cls(6)
        dumz.update(**dictionary)
        return dumz

    @classmethod
    def load_from_file(cls):
        """This method uses other methods to create a list of instances.

        Returns:
            list: an empty list if the file does not exits else it returns
                  a list of instances.

        """
        try:
            with open(cls.__name__ + '.json', 'r', encoding="UTF8") as d:
                newlist = cls.from_json_string(d.read())
                stuff = []

                for i in newlist:
                    data = cls.create(**i)
                    stuff.append(data)

                return stuff
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """This method implements csv(Comma Separated values)
        and saves a list of dictionaries to a file.

        Arg:
            list_objs(list): This contains a list of class objects.

        """
        dlist = []

        for i in list_objs:
            dlist.append(cls.to_dictionary(i))

        with open(cls.__name__ + '.csv', 'w', newline='') as csvfile:
            if cls.__name__ == "Rectangle":
                layout = ['id', 'width', 'height', 'x', 'y']

            else:
                layout = ['id', 'size', 'x', 'y']

            writer = csv.DictWriter(csvfile, fieldnames=layout)

            writer.writerows(dlist)

    @classmethod
    def load_from_file_csv(cls):
        """This method also implements csv to read from a file.

        Returns:
            list: A list of instances with all attributes already set.

        """
        with open(cls.__name__ + '.csv', 'r') as csvfile:
            if cls.__name__ == "Rectangle":
                layout = ['id', 'width', 'height', 'x', 'y']

            else:
                layout = ['id', 'size', 'x', 'y']

            reader = csv.DictReader(csvfile, fieldnames=layout)

            fi_list = []
            for i in reader:
                bict = {}
                for key, val in i.items():
                    bict.update({key: int(val)})
                fi_list.append(bict)

            bst_list = []
            for j in fi_list:
                info = cls.create(**j)
                bst_list.append(info)

            return bst_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """This method draws squares and rectangles passed.
        """
        wn = Screen().bgcolor("sky blue")
        shape('turtle')

        for i in list_rectangles:
            rect = i
            pensize(3)
            pencolor("dark red")
            up()
            setpos(rect.x, rect.y)
            down()
            for _ in range(2):
                fd(rect.width)
                rt(90)
                fd(rect.height)
                rt(90)

        for g in list_squares:
            sqr = g
            pensize(3)
            pencolor("dark green")
            up()
            setpos(sqr.x, sqr.y)
            down()
            for u in range(2):
                fd(sqr.size)
                lt(90)
                fd(sqr.size)
                lt(90)
        ht()
        done()
