#!/usr/bin/env python


import sys

points = {}

point_input = sys.stdin.readlines()

i = 0
while i < len(point_input):
    point = point_input[i].rstrip()
    # add point to dictio
    points[point] = True

    i += 1

# print points

first_line = " " + ("-" * 20) + " "

# insert plotting code

y = 19
x = 0

print " " + "-" * 20

while y > -1:
    # line = "|"
    grid = ["|"]
    x = 0
    while x < 20:

        coord = str(x) + " " + str(y)
        if coord in points:
            grid.append("*")
        else:
            grid.append(" ")

        x += 1
    # line += "|"
    # print line
    grid.append("|")
    new_grid = "".join(grid)
    print new_grid
    y -= 1

print " " + "-" * 20
