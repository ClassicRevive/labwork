#!/usr/bin/env python

#
#  Create a queue relying on a Stack. Actually Two Stacks.
#
#  The Stack ADT has three methods:
#     isempty(), push() and pop()
#
from Stack import Stack

class Queue(object):
    def __init__(self):
        # Initialise the queue
        self.s1 = Stack()
        self.s2 = Stack()


    def isempty(self):
        return self.s1.isempty() and self.s2.isempty()

    def enqueue(self, item):
        self.s1.push(item)

    def dequeue(self):
        if self.s2.isempty():
            while not self.s1.isempty():
                self.s2.push(self.s1.pop())
            return self.s2.pop()
        else:
            return self.s2.pop()


def main():
   q = Queue()

   command = input()
   while len(command) > 0:
      print(command + ":", end="")
      if command[0] == 'a': # add
         item = command.split()[1]
         q.enqueue(int(item));
      elif command[0] == 'r': # remove
         print(q.dequeue(), end="");
      else:
         print("Unknown command!")
      print(" _" if q.isempty() else " *")
      command = input()
   print()

if __name__ == "__main__":
   main()
