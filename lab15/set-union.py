#!/usr/bin/env python

import sys

seen = {}

# read from a.txt and b.txt
# add unseen elements of files to the list

with open("a.txt") as a:
    a_list = a.readlines()

    i = 0
    while i < len(a_list):
        word = a_list[i].rstrip()
        
        if word not in seen:
            seen[word] = True
        
        i += 1

with open("b.txt") as b:
    b_list = b.readlines()

    i = 0
    while i < len(b_list):
        word = b_list[i].rstrip()
        
        if word not in seen:
            seen[word] = True
        
        i += 1


for word in seen:
    sys.stdout.read(word)
