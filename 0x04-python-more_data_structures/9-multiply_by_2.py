#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdict = a_dictionary.copy()
    for k in newdict:
        newdict[k] *= 2
    return newdict
