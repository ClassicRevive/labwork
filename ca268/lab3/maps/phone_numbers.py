#!/usr/bin/env python3

import sys

logs = {}

print("Enter a name and number, or a name and ? to query (!! to exit)")
for line in sys.stdin:
    command = line.rstrip()
    if command == "!!":
        print("Bye")
        break
    elif command[-1] == "?":
        name = command.split()[0]
        try:
            print("{} has number {}".format(name, logs[name]))
        except KeyError:
            print("Sorry, there is no {}".format(name))
    else:
        name, num = command.split()
        logs[name] = num
