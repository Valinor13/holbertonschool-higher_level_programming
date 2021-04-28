#!/usr/bin/python3
import sys
if __name__ == '__main__':
    sumnum = 0
    for i in range(1, len(sys.argv)):
        sumnum += int(sys.argv[i])
    print("{:d}".format(sumnum))
