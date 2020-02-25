#!/usr/bin/env python3

''' return the fastest running time and name of runner '''

import sys

def seconds(t):
    mins, secs = t.split(":")

    return (60 * int(mins)) + int(secs)

def quickest(t):
    return seconds(t[1])

def main():
    runners = {}

    # firstly, for each runner find their fastest time and add to runners
    for runner in sys.stdin:
        runner = runner.rstrip().split()
        try:
            name, times = runner[0], runner[1:]
            fastest = min(times, key=seconds)
            runners[name] = fastest
        except:
            continue

    # items is list of tuples
    wname, wtime = (min(runners.items(), key=quickest))
    print('{} : {}'.format(wname, wtime))

if __name__ == '__main__':
    main()
