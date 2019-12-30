#!/usr/bin/env python

import os
import sys

files = os.listdir(".")

# i must now add a check wich reads each file and sees if the read is len 0
i = 0
while i < len(files):
    with open(files[i]) as file:
        s = file.read()
        if files[i][-3:] == ".py" and 0 < len(s):
            print files[i]

    i += 1
