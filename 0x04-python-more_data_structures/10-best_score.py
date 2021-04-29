#!/usr/bin/python3
def best_score(a_dictionary):
    if bool(a_dictionary) is False:
        return None
    max_key = max(a_dictionary, key=a_dictionary.get)
    return max_key
