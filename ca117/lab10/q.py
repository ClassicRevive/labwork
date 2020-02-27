#!/usr/bin/env python3

''' calculate each persons calorie intake from dictionary of calories '''

import sys
filename = sys.argv[1]

def gen_dictionary(file):
    f = {}
    with open(file) as fin:
        for line in fin:
            tokens = line.strip().rsplit(maxsplit=1)
            food, cals = (tokens[0], tokens[1])
            f[food] = int(cals)

        return f


def sorter(t):
    return t[1]


def main():
    foods = gen_dictionary(filename)
    people = {}
    
    for line in sys.stdin:
        tokens = line.strip().split(",")
        person, eaten = tokens[0], tokens[1:]
        people[person] = 0

        # count calories
        for food in eaten:
            if food in foods:
                people[person] += foods[food]
            else:
                people[person] += 100

    # longest lengths for cal numbers and names
    lperson = len(max(people.keys(), key=len))
    lfood = len(str(max(people.values())))
    
    for k, v in sorted(people.items(), key=sorter):
        print("{:>{:d}s} : {:{:d}d}".format(k, lperson, v, lfood))

if __name__ == '__main__':
    main()
