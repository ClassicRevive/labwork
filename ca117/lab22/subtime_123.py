#!/usr/bin/env python3

''' change 24 hour time by a given number of minutes '''

import sys


def hours2mins(t):
    h, m = t.split(":")
    h, m = int(h), int(m)
    if h == 0:
        h = 24
    return (60 * h) + m

def mins2hours(m):
    hours, minutes = divmod(m, 60)
    overflow, hours = divmod(hours, 24)

    time = '{:02d}:{:02d}'.format(hours, minutes)
    return time

def main():
    for line in sys.stdin:
        t, change = line.rstrip().split()
        change = int(change)

        # convert time to minutes, take away the change
        # then convert back to 24 hr time
        minutes = hours2mins(t)
        minutes -= change

        print(mins2hours(minutes))


if __name__ == '__main__':
    main()
