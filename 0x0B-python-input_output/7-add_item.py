#!/usr/bin/python3
"""This module makes use some imported functions; save_to_json_file and \
        load_from_json_file. This module also imports two other things; \
        os module and argv from the sys module. With these imports it is able \
        to create a list and write the list into a file. It is able to \
        continuously add values to the list.
"""
import os
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

dlist = []
for i in argv:
    if i == argv[0]:
        continue
    dlist += [i]

if os.path.exists("add_item.json"):
    read_info = load_from_json_file("add_item.json")
    if read_info != dlist:
        new_list = read_info + dlist
        save_to_json_file(new_list, "add_item.json")
        exit(1)

save_to_json_file(dlist, "add_item.json")
