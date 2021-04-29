#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if bool(a_dictionary) is False:
        return None
    keylist = a_dictionary.keys()
    sig = 0
    for i in keylist:
        if i == key:
            sig = 1
    if sig == 1:
        del a_dictionary[key]
    return a_dictionary
