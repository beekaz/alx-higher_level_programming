#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for integers in set(my_list):
        sum += integers
    return sum
