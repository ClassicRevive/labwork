#!/usr/bin/env python3

''' lay out leage data in matrix

POS CLUB                  P   W   D   L  GF  GA  GD PTS
  1 Chelsea              38  26   9   3  73  32  41  87
  2 Manchester City      38  24   7   7  83  38  45  79
  3 Arsenal              38  22   9   7  71  36  35  75
  4 Manchester United    38  20  10   8  62  37  25  70
  5 Tottenham Hotspur    38  19   7  12  58  53   5  64
  6 Liverpool            38  18   8  12  52  48   4  62
  7 Southampton          38  18   6  14  54  33  21  60
  8 Swansea City         38  16   8  14  46  49  -3  56
  9 Stoke City           38  15   9  14  48  45   3  54
 10 Crystal Palace       38  13   9  16  47  51  -4  48
 11 Everton              38  12  11  15  48  50  -2  47
 12 West Ham United      38  12  11  15  44  47  -3  47
 13 West Bromwich Albion 38  11  11  16  38  51 -13  44
 14 Leicester City       38  11   8  19  46  55  -9  41
 15 Newcastle United     38  10   9  19  40  63 -23  39
 16 Sunderland           38   7  17  14  31  53 -22  38
 17 Aston Villa          38  10   8  20  31  57 -26  38
 18 Hull City            38   8  11  19  33  51 -18  35
 19 Burnley              38   7  12  19  28  53 -25  33
 20 Queens Park Rangers  38   8   6  24  42  73 -31  30

 '''

import sys


def main():
    # find longest team name
    lines = sys.stdin.readlines()
    longest = 0
    for line in lines:
        line = line.strip().split()
        team = " ".join(line[1:-8])

        if longest < len(team):
            longest = len(team)

    header = "POS {:<{}s}  P   W   D   L  GF  GA  GD PTS".format("CLUB", longest)
    print(header)

    # now print out data accordingly
    # print each element of the list with correct formatting
    for line in lines:
        line = line.strip().split()
        team = " ".join(line[1:-8])
        POS = line[0]
        [P, W, D, L, GF, GA, GD, PTS] = line[-8:]
        print("{:>3s} {:{}s} {:>2s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s}"
              .format(POS, team, longest, P, W, D, L, GF, GA, GD, PTS))

if __name__ == '__main__':
    main()
