#!/usr/bin/env python


import sys
# this program changes the order of date
# in iris-dobs.txt and writes to american-dobs.txt


with open("irish-dobs.txt") as irish:
    s = irish.readline()
    while 0 < len(s):
        s_split = s.split()

        # reaggranging date
        date = s_split[0]
        date_parts = date.split("/")

        date_parts[0], date_parts[1] = date_parts[1], date_parts[0]

        first = "/".join(date_parts)  # joining date back together with "/"

        # joining name back together
        name = s_split[1:]
        second = " ".join(name)

        answer = first + " " + second + "\n"
        with open("american-dobs.txt", "a") as american:
            american.write(answer)

        s = irish.readline()
