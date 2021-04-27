#!/usr/bin/python3
def uppercase(str):
    newstr = ""
    for x in str:
        if ord(x) >= 97 and ord(x) <= 122:
            newstr += chr(ord(x) - 32)
        else:
            newstr += x
    print("{}".format(newstr))
