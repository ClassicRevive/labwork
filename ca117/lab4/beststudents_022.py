#!/usr/bin/env python3

'''print the name of students with highest mark and their mark
   now I need to check the file for non integer marks first'''

import sys
filename = sys.argv[1]


def main():
    marks = {}
    highest = 0
    highest_students = []
    
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
                        highest_students = [name]
                    elif highest == marks[name]:
                        highest_students.append(name)
                except ValueError:
                    print("Invalid mark {} encountered. Skipping.".format(mark))

        print("Best student(s): {:s}\nBest mark: {:d}".format(", ".join(highest_students), highest))
    except FileNotFoundError:
        print("The file {} could not be opened".format(filename))


if __name__ == '__main__':
    main()
