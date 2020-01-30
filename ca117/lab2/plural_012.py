#!/usr/bin/env python3

'''prints the plural of nouns which are passed in'''

import sys

alph = "abcdefghijklmnopqrstuvwxyz"
es = ["ch", "sh", "x", "s", "z"]
ies = []
for i in range(len(alph)):
    letter = alph[i]
    if letter not in "aeiou":
        ies.append(letter + "y")


def plural(s):
    if s[-2:] in es or s[-1] in es:
        return s + "es"
    elif s[-2:] in ies:
        return s[:-1] + "ies"
    elif s[-1] == "f":
        return s[:-1] + "ves"
    elif s[-2:] == "fe":
        return s[:-2] + "ves"
    elif s[-1] == "o":
        return s + "es"
    else:
        return s + "s"


def main():
    nouns = sys.stdin.readlines()
    for noun in nouns:
        noun = noun.rstrip()
        print(plural(noun))


if __name__ == '__main__':
    main()
