#!/usr/bin/env python3

''' print words which contain one instance of the vowels in traditional order '''

import sys

def main():
    matches = []
    for line in sys.stdin:
        word = line.rstrip()
        s = [c for c in word if c.lower() in "aeiou"]
        if "".join(s).lower() == "aeiou":
            matches.append(word)

    for match in matches:
        print(match)


if __name__ == '__main__':
    main()
