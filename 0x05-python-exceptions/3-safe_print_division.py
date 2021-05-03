#!/usr/bin/python3
def safe_print_division(a, b):
    if b is 0:
        print("Inside result: {}".format("None"))
        return None
    try:
       c = a / b
    except:
        print("Inside result: {}".format("None"))
        return None
    finally:
        print("Inside result: {:0.1f}".format(c))
        return c
