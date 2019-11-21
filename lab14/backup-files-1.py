#!/usr/bin/env python

import os
import sys

files = os.listdir(".")  # powerful!

i = 0
while i < len(files):
    # print files[i][-4:]
    if files[i][-4:] != ".bak":
        with open(files[i]) as ouu:
            s = ouu.read()  # read each file in files list
        with open(files[i] + ".bak", "w") as backup:
            backup.write(s)

    i += 1
