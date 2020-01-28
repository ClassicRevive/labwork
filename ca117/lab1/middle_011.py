#!/usr/bin/env python3


import sys

def main():
    lines = sys.stdin.readlines()

    for line in lines:
        line = line.strip()

        if len(line) % 2 == 1:
            print(line[len(line) // 2])
        else:
            print("No middle character!")


if __name__ == '__main__':
    main()
