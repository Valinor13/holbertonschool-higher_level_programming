#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if not my_list:
        return 0
    printcount = 0
    loopcount = 0
    while loopcount < x:
        if type(my_list[loopcount]) is int:
            try:
                print("{:d}".format(my_list[loopcount]), end="")
                printcount += 1
            except:
                print("", end="")
        else:
                print("", end="")
        loopcount += 1
    print()
    return printcount
