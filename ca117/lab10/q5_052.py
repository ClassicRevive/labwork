#!/usr/bin/env python3

''' display total marks of each student from stdin '''

import sys

def sorter(t):
    return int(t[1])

def main():
    marked = {}
    skipped = []

    for line in sys.stdin:
        try:
            name, marks = line.rstrip().split(":")
            marks = marks.split(",")

            # add up the persons grades
            total = 0
            for mark in marks:
                total += int(mark)

            marked[name] = total

        except ValueError:
            skipped.append(name)

    for (k, v) in sorted(marked.items(), key=sorter, reverse=True):
        print("{} : {}".format(k, v))

    if 0 < len(skipped):
        print("Skipped:")
        for person in skipped:
            print(person)


if __name__ == '__main__':
    main()
