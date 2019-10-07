#!/usr/bin/env python3

import sys


def nl_from_file(filename):
    f = open(filename, "r")
    row_num = 1
    for x in f:
        print(str(row_num) + "\t" + x, end="")
        row_num += 1

    f.close()


def nl_from_stdin():
    row_num = 1
    for line in sys.stdin:
        print(str(row_num) + "\t" + line.lstrip(), end="")
        row_num += 1
    print()


def main(args):
    if len(args) > 1:
        raise ValueError("too many file names")

    if len(args) == 1:
        nl_from_file(args)
    else:
        nl_from_stdin()



if __name__ == '__main__':
    main(sys.argv)
