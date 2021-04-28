#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    newlist = list()
    for x in range(len(my_list)):
        if x == idx:
            newlist.append(element)
        else:
            newlist.append(my_list[x])
    return newlist
