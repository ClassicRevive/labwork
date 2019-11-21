#!/usr/bin/env python

import os
import sys

files = os.listdir(".")

with open("start.txt") as start:
    s = start.read()
    print "hi"

print "hello"
isfile = os.path.isfile(s)

while isfile:
    with open(s) as hunt:
        s = hunt.read()

    isfile = os.path.isfile(s)

print s