#!/usr/bin/env python3

''' read names and numbers [and emails] into dictionary and query the dictionary from stdin '''

import sys

filename = sys.argv[1]


def main():
    contacts = {}

    with open(filename, "r") as fin:
        for line in fin:
            [name, num, email] = line.rstrip().split()
            contacts[name] = num, email

    for line in sys.stdin:
        name = line.rstrip()
        try:
            print('Name: {:s}\nPhone: {:s}\nEmail: {:s}'.format(name, contacts[name][0], contacts[name][1]))
        except:
            print("Name: {:s}\nNo such contact".format(name))


if __name__ == '__main__':
    main()
