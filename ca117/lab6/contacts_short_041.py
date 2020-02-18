#!/usr/bin/env python3

''' read names and numbers into dictionary and query the dictionary from stdin '''

import sys

filename = sys.argv[1]


def main():
    contacts = {}

    with open(filename, "r") as fin:
        for line in fin:
            [name, num] = line.rstrip().split()
            contacts[name] = num

    for line in sys.stdin:
        name = line.rstrip()
        try:
            print('Name: {}\nPhone: {}'.format(name, contacts[name]))
        except:
            print("Name: {}\nNo such contact".format(name))


if __name__ == '__main__':
    main()
