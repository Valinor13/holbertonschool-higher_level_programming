#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if bool(a_dictionary) is False:
        return None
    sig = 1
    while sig == 1:
        if bool(a_dictionary) is True:
            for k, v in a_dictionary.items():
                if v == value:
                    del a_dictionary[k]
                    sig = 1
                    break
                else:
                    sig = 0
        else:
            sig = 0
    return a_dictionary
