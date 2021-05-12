#!/usr/bin/python3
"""A module with the main function for the add item to list program"""


import json
import sys


stjf = __import__('5-save_to_json_file').save_to_json_file
lfjf = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
my_list = [lfjf(filename)]
for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])
stjf(my_list, filename)
