#!/usr/bin/env python


import sys
import os

boys_names = {}
girls_names = {}

names = sys.stdin.readlines()

# open boys names file and read names into dictionary
with open("boys.txt") as boys:
    b = boys.readlines()

    i = 0
    while i < len(b):
        name = b[i].rstrip()
        if name not in boys_names:
            boys_names[name] = True

        i += 1

# open girls names fuile and read names into dictionary
with open("girls.txt") as girls:
    g = girls.readlines()

    i = 0
    while i < len(g):
        name = g[i].rstrip()
        if name not in girls_names:
            girls_names[name] = True

        i += 1

# read stdin and compare with dictionaries
i = 0
while i < len(names):
    name = names[i].rstrip()
    if name in boys_names and name in girls_names:
        print name, "either"
    elif name in boys_names:
        print name, "boy"
    else:
        print name, "girl"

    i += 1
