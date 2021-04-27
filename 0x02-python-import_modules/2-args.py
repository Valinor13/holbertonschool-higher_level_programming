#!/usr/bin/python3
import sys
if __name__ == '__main__':
    x = len(sys.argv)
    if x == 1:
        print("{} arguments.".format(x - 1))
    elif x == 2:
        print("{} argument:".format(x - 1))
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(x - 1))
        for y in range(1, x):
            print("{:d}: {}".format(y, sys.argv[y]))
