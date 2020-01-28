#!/usr/bin/env python3


import sys


def main():
    lines = sys.stdin.readlines()
    for line in lines:
        words = line.rstrip().split(".")[:2]
        firstname = words[0].capitalize()
        surname = words[1]

        # linear searcg for number in email
        i = 0
        while i < len(surname) and (surname[i] < "0" or surname[i] > "9"):
            i += 1

        surname = words[1][:i].capitalize()
        print(firstname, surname)


if __name__ == '__main__':
    main()
