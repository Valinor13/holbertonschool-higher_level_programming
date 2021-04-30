#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if bool(a_dictionary) is False:
        return a_dictionary
    sig = 1
    while sig == 1:
        for k, v in a_dictionary.items():
            if v == value:
                del a_dictionary[k]
                break
            else:
                sig = 0
    return a_dictionary
