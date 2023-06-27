#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    number = 0
    try:
        for index in range(x):
            print(my_list[index], end='')
            number += 1
    except IndexError:
        None
    print()
    return number
