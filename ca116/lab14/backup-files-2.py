#!/usr/bin/env python

import os
import sys

files = os.listdir(".")  # powerful!

i = 0
while i < len(files):
    isfile = os.path.isfile(files[i])  # is the entry a file?

    if files[i][-4:] != ".bak" and isfile:  # if yes, and it is a backup
        with open(files[i]) as ouu:
            s = ouu.read()  # read each file in files list
        with open(files[i] + ".bak", "w") as backup:
            backup.write(s)

    i += 1
