#!/usr/bin/env python3

''' decode Jimmy encryption
    ie. for every vowel there is a "p" afterwards then the vowel again'''

import sys

def main():
    vowels = "aeiou"

    for line in sys.stdin:
        line = line.rstrip()
        decryption = ""

        i = 0
        while i < len(line):
            char = line[i]

            # for each vowel found, skip the next two characters
            if char in vowels:
                i += 2

            decryption += char
            i += 1

        print(decryption)

if __name__ == '__main__':
    main()
