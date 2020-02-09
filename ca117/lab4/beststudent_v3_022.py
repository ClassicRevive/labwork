#!/usr/bin/env python3

'''print the name of student with highest mark and their mark (with exception handling)'''

import sys
filename = sys.argv[1]


def main():
    marks = {}
    highest = 0
    highest_student = ""
    try:
        with open(filename, "r") as fin:
            for line in fin:
                try:
                    # split line into tokens and add data to dictionary
                    tokens = line.strip().split()
                    [mark, name] = [tokens[0], " ".join(tokens[1:])]
                    marks[name] = int(mark)

                    if highest < marks[name]:
                        highest = marks[name]
                        highest_student = name
                except ValueError:
                    print("Invalid mark {} encountered. Skipping.".format(mark))

        print("Best student: {:s}\nBest mark: {:d}".format(highest_student, highest))
    except FileNotFoundError:
        print("The file {} could not be opened".format(filename))


if __name__ == '__main__':
    main()
