#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printcount = 0
    loopcount = 0
    for loopcount in range(x):
        try:
            print("{:d}".format(my_list[loopcount]), end="")
            printcount += 1
        except IndexError:
            break
        except:
            continue
        loopcount += 1
    print()
    return printcount
