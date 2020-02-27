#!/usr/bin/env python3

''' count each persons calories from stdin based on calories data'''

import sys

def sort_on(t):
    return t[1]

def gen_file_dictionary(f):
        d = {}
        with open(f) as fin:
            for line in fin:
                tokens = line.rstrip().rsplit(maxsplit=1)
                food, cal = tokens[0], int(tokens[1])
                d[food] = cal

        return d


def main():
    filename = sys.argv[1]
    people = {}
    cals = gen_file_dictionary(filename)

    for line in sys.stdin:
        tokens = line.rstrip().split(",")
        person, foods = tokens[0], tokens[1:]
        people[person] = 0

        for food in foods:
            if food in cals:
                people[person] += cals[food]
            else:
                people[person] += 100

    # person column width = longest name
    lperson = len(max(people.keys(), key=len))
    lfood = len(str(max(people.values())))
    # food column width = length of highest number in string form
    for person, food in sorted(people.items(), key=sort_on):
        print("{:>{:d}s} : {:{}d}".format(person, lperson, food, lfood))


if __name__ == '__main__':
    main()
