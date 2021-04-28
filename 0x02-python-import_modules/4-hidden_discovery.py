#!/usr/bin/python3
import hidden_4
if __name__ == '__main__':
    for x in dir(hidden_4):
        if x.startswith("__") is True:
            continue
        else:
            print("{}".format(x))
