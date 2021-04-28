#!/usr/bin/python3
def no_c(my_string):
    newstr = ""
    for x in my_string:
        if x == 'c' or x == 'C':
            continue
        else:
            newstr += x
    return newstr
