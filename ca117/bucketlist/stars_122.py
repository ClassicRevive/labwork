#!/usr/bin/env python

# count starts using matching algorithm

import sys

# read map into a matrix using nested list data type

def gen_map(rows):
    starmap = []
    for i in range(rows):
        row = sys.stdin.readline().rstrip()
        starmap.append(row)

    return starmap


def find_star(i, j, plane):
    point = (i, j)
    to_search = []
    to_search.append(point)

    while to_search != []:  # while there are points to search, continue
        p = to_search.pop()
        i = p[0]
        j = p[1]

        lstar = (p[0], p[1] - 1)
        rstar = (p[0], p[1] + 1)
        dstar = (p[0] + 1, p[1])
        ustar = (p[0] - 1, p[1])
        # look all around each point for another "-"
        if p[0] - 1 >= 0 and plane[ustar[0]][ustar[1]] == "-":
            to_search.append(ustar)

        if p[1] - 1 >= 0 and plane[lstar[0]][lstar[1]] == "-":
            to_search.append(lstar)

        if p[0] + 1 < len(plane) and plane[dstar[0]][dstar[1]] == "-":
            to_search.append(dstar)

        if p[1] + 1 < len(plane[i]) and plane[rstar[0]][rstar[1]] == "-":
            to_search.append(rstar)

        # UPDATE THE STAR PLANE ITSELF INSTEAD OF A LIST
        line = plane[i]
        new = line[:j] + "*" + line[j + 1:]
        plane[i] = new

    return plane


def main():
    mxn = sys.stdin.readline().split()
    r, c = int(mxn[0]), int(mxn[1])
    starm = gen_map(r)

    starcount = 0

    for row in range(len(starm)):
        col = 0
        while col < c:
            # when "-" is found, find the whole star and update the map
            if starm[row][col] == "-":
                starm = find_star(row, col, starm)
                starcount += 1

            col += 1

    print(starcount)

if __name__ == '__main__':
        main()
