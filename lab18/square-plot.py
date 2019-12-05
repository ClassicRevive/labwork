#!/usr/bin/env python


import sys

x_y_length = sys.argv[1:]

# print points

first_line = " " + ("-" * 20) + " "

# insert plotting code

def should_plot(x, y):
    global length

    x = x_y_length[0]
    y = x_y_length[1]
    length = x_y_length[2]

    if 



def generate_grid():
    y = 19
    x = 0

    while y > -1:
        # line = "|"
        grid = ["|"]
        x = 0
        while x < 20:

            coord = str(x) + " " + str(y)
            if should_plot():
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

generate_grid()

print " " + "-" * 20
