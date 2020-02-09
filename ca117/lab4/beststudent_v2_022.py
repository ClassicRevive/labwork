#!/usr/bin/env python3

'''print the name of student with highest mark and their mark
   now I need to check the file for non integer marks first'''

import sys
filename = sys.argv[1]


def main():
    marks = {}
    highest = 0
    highest_student = ""
    try:
        with open(filename, "r") as fin:
            for line in fin:
                # split line into tokens and add data to dictionary
                tokens = line.strip().split()
                [mark, name] = [tokens[0], " ".join(tokens[1:])]
                marks[name] = int(mark)

                if highest < marks[name]:
                    highest = marks[name]
                    highest_student = name

        print("Best student: {:s}\nBest mark: {:d}".format(highest_student, highest))
    except FileNotFoundError:
        print("The file {} could not be opened".format(filename))
    except ValueError:
        print("Invalid mark {:s} encountered. Exiting.".format(mark))


if __name__ == '__main__':
    main()
