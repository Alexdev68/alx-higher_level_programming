#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        dlist = []
        for L1, l2 in zip(my_list_1, my_list_2):
            if type(L1) != (int or float) or type(l2) != (int or float):
                dlist.append(0)
                print("wrong type")
                continue
            if l2 == 0:
                dlist.append(0)
                print("division by 0")
                continue
            dlist.append(L1 / l2)
        if len(dlist) < list_length:
            remains = list_length - len(dlist)
            print("out of range")
            i = 0
            while i < remains:
                dlist.append(0)
                i += 1

    except (TypeError, ZeroDivisionError, IndexError):
        pass
    finally:
        return dlist
