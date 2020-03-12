#!/usr/bin/env python

# count starts using matching algorithm

import sys

# read map into a matrix using nested list data type

def gen_map(rows, columns):
    starmap = []
    for i in range(rows):
        row = sys.stdin.readline()
        row = list(row.rstrip())
        # print(row)
        starmap.append(row)

    return starmap


def main():
    mxn = sys.stdin.readline().split()
    r, c = int(mxn[0]), int(mxn[1])
    starm = gen_map(r, c)

    # find every single "-" first
    seen_chords = []
    for row in range(len(starm)):
        col = 0
        while col < c:
            if starm[row][col] == "-":
                seen_chords.append((row, col))

            col += 1


    while 0 < len(seen_chords):
        curr_star = [p]
        
        # eliminate star points out of seen chords in clusters
        # using <v> directional search

        i = 0
        while i < len(curr_star):
            lstar = (curr_star[i][0] - 1, curr_star[i][1])
            rstar = (curr_star[i][0] + 1, curr_star[i][1])
            dstar = (curr_star[i][0], curr_star[i][1] - 1)

            if lstar in seen_chords:
                curr_star.append(lstar)
            elif rstar in seen_chords:
                curr_star.append(rstar)
            elif dstar in seen_chords:
                curr_star.append(rstar)
            
            i += 1

        for coord in curr_star:
            seen_chords.remove(coord)

    print(seen_chords)

if __name__ == '__main__':
        main()
