#!/usr/bin/env python


import sys

x_y_length = sys.argv[1:]
length = int(x_y_length[2])
# print points

first_line = " " + ("-" * 20) + " "

# insert plotting code
bot_left = x_y_length[0] + " " + x_y_length[1]

def should_plot(bottom_left, point):

    x = int(x_y_length[0])
    y = int(x_y_length[1])

    point = point.split()

    i = 0
    while i < len(point):
        point[i] = int(point[i])
        i += 1

    if point[0] == x and point[1] == y + length - 1:
        return "top_or_bot"

    if point[0] == x and point[1] < (y + length - 1) and point[1] > y:
        return "mid"

    if point[0] == x and point[1] == y:
        return "top_or_bot"

def generate_grid():
    y = 19
    x = 0

    while y > -1:
        # line = "|"
        grid = ["|"]
        x = 0
        while x < 20:

            coord = str(x) + " " + str(y)

            if should_plot(bot_left, coord) == "top_or_bot":
                grid.append("*" * length)
                x = x + length - 1
            elif should_plot(bot_left, coord) == "mid":
                grid.append("*" + (" " * (length - 2)) + "*")
                x = x + length - 1

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
