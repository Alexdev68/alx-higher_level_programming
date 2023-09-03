#!/usr/bin/python3
"""This module contains a function that finds a peak in a list fo integers.
"""


def find_peak(list_of_integers):
    """This function finds a peak in a list fo integers.
    """
    if (list_of_integers == []):
        return None

    dlist = list_of_integers

    left, right = 0, len(dlist) - 1

    while left < right:
        mid = (left + right) // 2

        if dlist[mid] < dlist[mid + 1]:
            left = mid + 1

        else:
            right = mid

    return dlist[left]
