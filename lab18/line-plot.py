#!/usr/bin/env python


import sys

point_1 = sys.argv[0] + "-" + sys.argv[2]
point_2 = sys.argv[1] + "-" + sys.argv[3]



first_line = " " + ("-" * 20) + " "

# insert plotting code
bot_left = x_y_length[0] + " " + x_y_length[1]

def should_plot():

    
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
