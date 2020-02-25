#!/usr/bin/env python3

'''given a number of lines containing names of racers and their times
   stdout should print the name of the racer with the fastest time
   along with their fastest time.
   '''

import sys

# last min is based on this sort
def sorter(t):
    return seconds(t[-1])

# convert string time to seconds
def seconds(t):
    m, s = t.split(":")
    return int(m) * 60 = int(s)

def main():
    d = {}
    
    for line in sys.stdin:
        try:  # exception handler for illegal values
            tokens = line.strip().split()
            name, times = tokens[0], tokens[1:]
            d[name] = min(times, key=seconds)
        except ValueError:
            continue # or pass (break will exit the for loop)

    wname, wtime = min(d.items(), key=sorter)
    print("{} : {}".fomrat(wname, wtime))


if __name__ == '__main__':
    main()