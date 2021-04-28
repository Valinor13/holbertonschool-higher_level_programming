#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    biggie = my_list[0]
    for x in my_list:
        if x > biggie:
            biggie = x
    return biggie
