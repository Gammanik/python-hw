# #!/usr/bin/env python3

import sys


def wc_from_files(filenames):
    total_lines: int = 0
    total_words: int = 0
    total_bytes: int = 0

    for filename in filenames:
        lines: int = 0
        words: int = 0
        bytes: int = 0

        f = open(filename, "r")

        for line in f:
            lines += 1
            for word in line.split():
                words += 1
            for symbol in line:
                bytes += len(symbol.encode('utf-8'))

        print("%d %d %d %s" % (lines, words, bytes, filename))
        total_lines, total_words = total_lines + lines, total_words + words
        total_bytes += bytes
        f.close()

    if len(filenames) > 1:
        print("%d %d %d total" % (total_lines, total_words, total_bytes))


def wc_from_stdin():
    lines: int = 0
    words: int = 0
    bytes: int = 0

    for line in sys.stdin:
        lines += 1

        for word in line.split():
            words += 1
        for symbol in line:
            bytes += len(symbol.encode('utf-8'))

    print("      %d      %d     %d" % (lines, words, bytes))


def main(args):
    if len(args) > 0:
        wc_from_files(args)
    else:
        wc_from_stdin()


if __name__ == '__main__':
    main(sys.argv[1:])
