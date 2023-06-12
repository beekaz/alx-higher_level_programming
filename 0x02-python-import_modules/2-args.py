#!/usr/bin/python3
import sys

argc = len(sys.argv) - 1

if __name__ == "__main__":
    if argc == 0:
        print("0 arguments.")
    else:
        print("{} argument{}".format(argc, "s" if argc > 1 else ""))
        for i in range(1, len(sys.argv)):
            print("{:d}: {:s}".format(i, sys.argv[i]))
