#!/usr/bin/env python

a = []
b = []

s = raw_input()
while s != "end":
    a.append(s)
    s = raw_input()

s = raw_input()
while s != "end":
    b.append(s)
    s = raw_input()

if len(b) != 0:
    if b[-1] == "":
        b.pop()

    i = 0
    string = ""
    while i < len(b):
        if b[i] == "":
            string = string + "\n"  # \n is 1 length not 2
            # print string
        elif string == "" or string[-1] == "\n":
            string = string + a[int(b[i])]
            # print string
        else:
            string = string + " " + a[int(b[i])]
            # print string

        i += 1

    print string
