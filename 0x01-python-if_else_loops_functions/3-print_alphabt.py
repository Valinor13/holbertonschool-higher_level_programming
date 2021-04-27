#!/usr/bin/python3
for x in range(97, 123):
    if x == 101:
        x += 1
    elif x == 113:
        x += 1
    else:
        print("{}".format(chr(x)), end="")
