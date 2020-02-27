#!/usr/bin/env python3

''' return words which contain a single instance of aeiou '''

import sys

def main():
    vowels = "aeiou"
    for line in sys.stdin:
        line = line.rstrip()

        test = [c for c in line if c.lower() in vowels]
        test_string = "".join(test)

        if test_string.lower() == vowels:
            print(line)

if __name__ == '__main__':
    main()
