#!/usr/bin/env python


import sys

# take inputs
# make dictionary
status = {}
counter = {}
tasks = sys.stdin.readlines()

i = 0
while i < len(tasks):
    # split into sections
    task = tasks[i].rstrip()
    task_split = task.split(".")

    # isolate userame
    key = task_split[0]
    value = task_split[2]

    status[key] = value == "correct"

    i += 1

# print status

# now count how many Trues for each user
# to do this, use another dictionary
# loop through first dictionary usinf "for" loop
# isolate username from key of status

for preuser in status:
    # isolate username from key of status
    user = preuser.split("/")[0]

    # add username to counter dictionary
    if user not in counter:
        counter[user] = 0

    # count True's for each username
    if status[preuser]:
        counter[user] += 1

for user in counter:
    print user, "correct count:", counter[user]
