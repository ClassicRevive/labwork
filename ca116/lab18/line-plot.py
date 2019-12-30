#!/usr/bin/env python


import sys

# take points as list tuples from argv
point_1 = sys.argv[1:3]
point_2 = sys.argv[3:]

# convert to integers for calculation
i = 0
while i < len(point_1):
    point_1[i] = float(point_1[i])
    i += 1

i = 0
while i < len(point_2):
    point_2[i] = float(point_2[i])
    i += 1

# insert plotting code

first_line = " " + ("-" * 20) + " "

# my should_plot does not work when the slope is negative
def should_plot(point1, point2, grid_point):
    slope = (point2[1] - point1[1]) / (point2[0] - point1[0])
    constant = point1[1] - (slope * point1[0])
    y = (slope * grid_point[0]) + constant + 0.5
    x = (grid_point[1] - constant) / slope + 0.5
    x = int(x)
    y = int(y)

    # if grid_point == point1 or grid_point == point2:
    #     return "plot"

    # print "x", x
    # print "y", y
    if grid_point[0] < point1[0] and grid_point[0] < point2[0]:  # too left
        return False
    elif grid_point[0] > point1[0] and grid_point[0] > point2[0]:  # too right
        return False
    elif grid_point[1] > point1[1] and grid_point[1] > point2[1]:  # too up
        return False
    elif grid_point[1] < point1[1] and grid_point[1] < point2[1]:  # too down
        return False
    else:
        if grid_point[0] == x or grid_point[1] == y:
            return "plot"


def generate_grid():
    y = 19
    x = 0

    while y > -1:
        # line = "|"
        grid = ["|"]
        x = 0
        while x < 20:

            coord = [x, y]

            if should_plot(point_1, point_2, coord) == "plot":
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
