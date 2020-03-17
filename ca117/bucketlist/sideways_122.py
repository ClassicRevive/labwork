#!/usr/bin/env python3

''' sort columbna alphabetically sideways and print result '''

import sys

def alpha(s):
    return s.lower()


def main():

    # firstly, add first letter of each word to list for indexing
    columns = []

    init = sys.stdin.readline().rstrip()
    for letter in init:
        columns.append(letter)

    # now add the rest of columns
    cols = len(init)
    for line in sys.stdin:
        i = 0
        while i < cols:
            columns[i] += line[i]

            i += 1

    # now sort the columns in alphabetical order
    columns = sorted(columns, key=alpha)
    # print(columns)

    # now print the words in column format!
    j = 0
    while j < len(columns[0]):
        line = ""
        for word in columns:
            line += word[j]

        print(line)

        j += 1


if __name__ == '__main__':
    main()
