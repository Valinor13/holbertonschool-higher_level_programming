#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    loopcount = 0
    printcount = 0
    while loopcount < x:
        try:
            print("{}".format(my_list[loopcount]), end="")
            printcount += 1
        except:
            print()
            return printcount
        finally:
            loopcount += 1
    print()
    return printcount
