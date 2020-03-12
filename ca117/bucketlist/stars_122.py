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


def main():
    mxn = sys.stdin.readline().split()
    r, c = int(mxn[0]), int(mxn[1])
    starm = gen_map(r)

    # find every single "-" first
    star_coords = []
    for row in range(len(starm)):
        col = 0
        while col < c:
            if starm[row][col] == "-":
                star_coords.append((row, col))

            col += 1

    starcount = 0
    while 0 < len(star_coords):
        # eliminate star points out of seen chords in clusters
        # using < v > directional search

        # print(star_coords)
        i = 0
        curr_star = [star_coords[i]]
        while i < len(curr_star):
            lstar = (curr_star[i][0], curr_star[i][1] - 1)
            rstar = (curr_star[i][0], curr_star[i][1] + 1)
            dstar = (curr_star[i][0] + 1, curr_star[i][1])

            if lstar not in curr_star and lstar in star_coords:
                curr_star.append(lstar)
            if rstar not in curr_star and rstar in star_coords:
                curr_star.append(rstar)
            if dstar not in curr_star and dstar in star_coords:
                curr_star.append(dstar)

            # print(curr_star)

            i += 1

        star_coords = [s for s in star_coords if s not in curr_star]

        starcount += 1

    print(starcount)

if __name__ == '__main__':
        main()
