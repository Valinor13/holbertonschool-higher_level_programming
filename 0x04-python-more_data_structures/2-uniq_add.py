#!/usr/bin/python3
def uniq_add(my_list=[]):
    if bool(my_list) is False:
        return 0
    newset = set(my_list)
    sumnum = sum(newset)
    return sumnum
