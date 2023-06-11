#!/usr/bin/python3
"""This module contains a class that prints a sorted list.
"""


class MyList(list):
    """This class print a sorted list in ascending order.
    """
    def print_sorted(self):
        """This method prints the sorted list.
        """
        print(sorted(self))
