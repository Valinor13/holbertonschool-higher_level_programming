#!/usr/bin/python3
import hidden_4
if __name__ == '__main__':
    newdir = dir(hidden_4)
    length = len(newdir)
    for x in range(length):
        if newdir[x][0] == '_' and newdir[x][1] == '_':
            continue
        else:
            print("{}".format(newdir[x]))
