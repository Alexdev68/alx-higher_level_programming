#!/usr/bin/python3
def search_replace(my_list, search, replace):
    dlist = []
    for i in my_list:
        if i == search:
            i = replace
        dlist.append(i)

    return dlist
