#!/usr/bin/python3
for x in range(99):
    print("{:d}{:d},".format(x // 10, x % 10), end=" ")
    x += 1
print("{:d}".format(x))
