#!/usr/bin/env python3

import sys

def replace_white(i, j, sky, lines):
    point = ":".join([str(i), str(j)])
    left = []
    left.append(point)

    while left != []:
        p = left.pop()

        i, j = int(p.split(":")[0]), int(p.split(":")[1])

        if i - 1 >= 0:
            if sky[i - 1][j] == "-":
                left.append(str(i - 1) + ":" + str(j))

        if j - 1 >= 0:
            if sky[i][j - 1] == "-":
                left.append(str(i) + ":" + str(j - 1))

        if j + 1 <= len(sky[i]) - 1:
            if sky[i][j + 1] == "-":
                left.append(str(i) + ":" + str(j + 1))

        if i + 1 < len(sky):
            if sky[i + 1][j] == "-":
                left.append(str(i + 1) + ":" + str(j))

        line = sky[i]
        new = line[:j] + "*" + line[j + 1:]
        sky[i] = new

    return sky

def main():
    n, m = sys.stdin.readline().strip().split()
    n, m = int(n), int(m)

    sky = []
    for line in sys.stdin:
        sky.append(line.strip())

    total_stars = 0

    for i in range(0, n):
        for j in range(0, m):
            if sky[i][j] == "-":
                sky = replace_white(i, j, sky, n)
                total_stars += 1

    print(total_stars)


if __name__ == '__main__':
    main()