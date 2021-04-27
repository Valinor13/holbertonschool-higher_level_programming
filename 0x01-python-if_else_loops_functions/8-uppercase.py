#!/usr/bin/python3
def uppercase(str):
    length = len(str)
    for x in range(length):
        if ord(str[x]) >= 97 and ord(str[x]) <= 122:
            print("{}".format(chr(ord(str[x]) - 32)), end="")
        else:
            print("{}".format(str[x]), end="")
