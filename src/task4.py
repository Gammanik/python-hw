# #!/usr/bin/env python3

import sys
from collections import deque


def tail_from_stdin():
    d = deque()

    for x in sys.stdin:
        if len(d) >= 10:
            d.popleft()

        d.append(x)

    for el in d:
        print(el, end="")


def tail_from_files(filenames):
    for filename in filenames:
        f = open(filename, "r")
        d = deque()

        for x in f:
            if len(d) >= 10:
                d.popleft()

            d.append(x)

        if len(filenames) > 1:
            print("==> %s <==" % filename)

        for el in d:
            print(el, end="")

        f.close()


def main(args):
    if len(args) > 1:
        raise ValueError("too many file arguments")

    if len(args) == 1:
        tail_from_files(args)
    else:
        tail_from_stdin()


if __name__ == '__main__':
    main(sys.argv)
