#!/usr/bin/python3
for number in range(0, 99):
    print("{number:d} = {hex_dec}".format(
        number=int(number), hex_dec=hex(number)), end="\n")
