#!/usr/bin/env python3

'''read stdin until a number input. Once a number is found. print Thank you.'''

import sys

def main():
    try:
        for line in sys.stdin:
            line = line.rstrip()
            if line.isdigit():
                line = int(line)

            print("{:s} is not a number".format(line))

    except ValueError:
        print("Thank you for {:d}".format(line))


if __name__ == '__main__':
    main()
