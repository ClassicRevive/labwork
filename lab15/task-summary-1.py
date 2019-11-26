#!/usr/bin/env python


#!/usr/bin/env python

import sys

# take inputs
# make dictionary
status = {}
tasks = sys.stdin.readlines()

i = 0
while i < len(tasks):
    task = tasks[i].rstrip()
    task_split = task.split(".")
    # print task_split
    key = task_split[0] + "." + task_split[1]
    value = task_split[2]

    status[key] = value == "correct"

    i += 1

for key in status:
    if status[key]:
        print key
