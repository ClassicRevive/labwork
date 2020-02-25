#!/usr/bin/env python3


'''reads a string from the command line and swaps all adjacent 
   characters in the string and prints the result.'''


import sys
word = sys.argv[1]


def adj(s):
    i = 0
    while i < len(s) - 1:
        s[i], s[i + 1] = s[i + 1], s[i]

        i += 2

    return "".join(s)


def main():
    a = list(word)

    print(adj(a))


if __name__ == '__main__':
    main()
