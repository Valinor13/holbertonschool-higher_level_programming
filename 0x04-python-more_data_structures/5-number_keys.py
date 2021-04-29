#!/usr/bin/python3
def number_keys(a_dictionary):
    if bool(a_dictionary) == False:
        return 0
    count = 0
    for x in a_dictionary:
        count += 1
    return count
