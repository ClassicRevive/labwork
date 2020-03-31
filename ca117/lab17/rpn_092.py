#!/usr/bin/env python3

from stack_092 import Stack
import operator

def calculator(line):
    binops = {"+": operator.add,
              "-": operator.sub,
              "*": operator.mul,
              "/": operator.truediv}

    uniops = {"n": operator.neg,
              "r": operator.pow}

    line = line.split()
    numbers = Stack()

    # convert numbers to float
    i = 0
    while i < len(line) and line[i] not in binops and line[i] not in uniops:
        line[i] = float(line[i])
        i += 1

    # run through the line and complete operations using stack
    for token in line:
        if type(token) is float:
            numbers.push(token)
        elif token in binops:
            t1 = numbers.pop()
            t2 = numbers.pop()
            op = binops[token]
            
            numbers.push(op(t2, t1))
        elif token in uniops:
            t = numbers.pop()
            if token == "r":
                op = uniops["r"]
                ans = op(t, 0.5)
            else:
                op = uniops[token]
                ans = op(t)

            numbers.push(ans)

    return numbers.top()
