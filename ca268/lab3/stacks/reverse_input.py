import sys
from stack import Stack

def reverse_input(s):
    for line in sys.stdin:
        line = line.rstrip()
        s.push(line)

    while not s.is_empty():
        print(s.pop())

stack = Stack()
reverse_input(stack)