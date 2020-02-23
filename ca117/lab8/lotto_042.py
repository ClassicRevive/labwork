#!/usr/bin/env python3

''' use simulation to calculate odds of different scores
    in irish lottery '''

import random
import sys

cmd_draw = set(sys.argv[1:])
# print(cmd_draw)

def main():
    matches = {"Match3": 0,
               "Match4": 0,
               "Match5": 0,
               "Match6": 0}

    # generate random draw sets and compare to our lucky set
    
    for i in range(1000000):
        rand_draw = set()
        seen = set()

        # generate 
        while len(rand_draw) < 6:
            number = str(random.randrange(1, 48))
            
            if number not in seen:
                rand_draw.add(number)
                seen.add(number)
        
        # test for the number of number matches between our draw
        # and the random draw
        if 2 < len(cmd_draw.intersection(rand_draw)):
            matchno = str(len(cmd_draw.intersection(rand_draw)))
            matches["Match" + matchno] += 1

    # get longest number for right justification format
    longest = 0
    for match in matches:
        if longest < len(str(matches[match])):
            longest = len(str(matches[match]))

    for match in sorted(matches):
        matchcount = matches[match]
        
        if matchcount != 0:
            odds = int((1000000 / matchcount) + 0.5)
        else:
            odds = "?"
        
        mn = match[-1]
        print("Match {:s}'s: {:>{:d}d} ({} to 1)".format(mn, matchcount, longest, odds))






if __name__ == '__main__':
    main()






