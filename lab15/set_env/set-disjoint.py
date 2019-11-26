#!/usr/bin/env python

import sys

a_dict = {}
# b_dict = {}

# read from a.txt and b.txt
# add unseen elements of files to the list

with open("a.txt") as a:
    a_list = a.readlines()
    i = 0
    while i < len(a_list):
        word = a_list[i].rstrip()

        if word not in a_dict:
            a_dict[word] = True

        i += 1

intersection = False

with open("b.txt") as b:
    b = sys.stdin.readlines()
    i = 0
    while i < len(b) and not(intersection):
        word = b[i].rstrip()

        if word in a_dict:
            intersection = True
        i += 1


if intersection:
    print "intersecting"
else:
    print "disjoint"

"""
with open("b.txt") as b:
    b_list = b.readlines()

    i = 0
    while i < len(b_list):
        word = b_list[i].rstrip()

        if word not in b_dict:
            b_dict[word] = True

        i += 1
"""
