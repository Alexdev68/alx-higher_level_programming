#!/usr/bin/python3
"""This module contains a class ``MyInt``.
"""


class MyInt(int):
    """This class is a rebel and it changes equal to, to not equal to and \
            vice versa.
    """

    def __eq__(self, other):
        """This method changes equal to, to not equal to.
        """
        return self.real != other

    def __ne__(self, other):
        """This method changes not equal to, to equal to.
        """
        return self.real == other
