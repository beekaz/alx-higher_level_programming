#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
        my_list.sort()
        my_list.reverse()
        for integers in my_list:
            print("{:d}".format(int(integers)))
