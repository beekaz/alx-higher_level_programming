#!/usr/bin/python3
for ascii_numbers in range(97, 123):
    if chr(ascii_numbers) not in ['q', 'e']:
        print("{alphabet}".format(alphabet=chr(ascii_numbers)), end="")
