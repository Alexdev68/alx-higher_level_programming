#!/usr/bin/python3
"""This module contains a function that finds a peak in a list fo integers.
"""

def find_peak(list_of_integers):
    """This function finds a peak in a list fo integers.
    """
    dlist = list_of_integers

    lent = len(dlist) - 1

    for i in range(len(dlist)):
        if i == 0 and dlist[i] >= dlist[1]:
            return dlist[i]
        
        elif i == lent and dlist[i] >= dlist[lent - 1]:
            return dlist[i]

        elif dlist[i + 1] <= dlist[i] and dlist[i - 1] <= dlist[i]:
            return dlist[i]
