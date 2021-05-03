#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for loopcount in range(list_length):
        try:
            result = my_list_1[loopcount] / my_list_2[loopcount]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except:
            result = 0
        finally:
