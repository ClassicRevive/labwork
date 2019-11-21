#!/usr/bin/env python

import os
import sys

files = os.listdir(".")

with open("start.txt") as start:
    s = start.read().rstrip()


isfile = os.path.isfile(s)
# print isfile

while isfile:
    with open(s) as hunt:
        s = hunt.read().rstrip()

    isfile = os.path.isfile(s)

print s
