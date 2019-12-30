#!/usr/bin/env python


if __name__ == "__main__":
    import sys
    filename = sys.argv[1]
    words = sys.argv[2:]

with open(filename, "w") as fd:
    i = 0
    while i < len(words):
        fd.write(words[i] + "\n")
        i += 1
