#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return None
    newset = set(my_list)
    sumnum = sum(newset)
    return sumnum
