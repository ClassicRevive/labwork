#!/usr/bin/env python


import os
import sys
# this program should parse list of files
# enter directories in the pwd and list there files
# i need a general loop which continues to enter new directories if the exist.
files = os.listdir(".") 

i = 0  # the problem with this program is that it can only enter one directory.
directories = []
while i < len(files):
    isfile = os.path.isfile(files[i])
    
    if isfile:
        print "./" + files[i]
    else:
        directories.append("./" + files[i])

    i += 1

# print directories

while len(directories) != 0:
    i = 0
    while i < len(directories):
        dir_files = os.listdir(directories[i])

        j = 0
        while j < len(dir_files):
            isfile = os.path.isfile(directories[i] + "/" + dir_files[j])

            if isfile:
                print directories[i] + "/" + dir_files[j]
            else:
                directories.append(directories[i] + "/" + dir_files[j])

            j += 1

        directories.pop(i)
        i += 1