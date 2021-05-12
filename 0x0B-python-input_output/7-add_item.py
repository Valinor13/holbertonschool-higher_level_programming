#!/usr/bin/python3
"""A module with the main function for the add item to list program"""


import json
import sys


stjf = __import__('5-save_to_json_file').save_to_json_file
lfjf = __import__('6-load_from_json_file').load_from_json_file
if __name__ == "__main__":

    my_list = []
    my_string = ""
    filename = "add_item.json"
    try:
        f = open(filename, "x")
        f.close()
        f = open(filename, "w")
        f.write(my_string)
        f.close()
    except:
        with open(filename) as f:
            if f.seek(0) is "":
                f.close()
            else:
                my_string = lfjf(filename)
    my_list.append([my_string])
    for i in range(1, len(sys.argv)):
        my_list.append(str(sys.argv[i]))
    stjf(my_list, filename)
