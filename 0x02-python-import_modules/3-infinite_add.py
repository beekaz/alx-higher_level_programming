#!/usr/bin/python3
import sys

argc = len(sys.argv) - 1

def sum_args():
    total_sum = 0
    for i in range(1, len(sys.argv)):
        total_sum += int(sys.argv[i])
    return total_sum

if __name__ == "__main__":
    if argc == 0:
        print("{:d}".format(argc))
    else:
        print("{:d}".format(sum_args()))
