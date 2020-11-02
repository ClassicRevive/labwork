#!/usr/bin/env python3
from Queue import Queue

def print_queue(lst, front, back):
    q = Queue()
    q_list =[]
    q.data, q.front, q.back = lst, front, back

    while not q.isempty():
        q_list.append(q.dequeue())

    return q_list

def main():
   size = int(input())
   q = Queue(size)

   command = input()
   while len(command) > 0:
      if command[0] == 'a': # add
         item = command.split()[1]
         q.enqueue(int(item));
      elif command[0] == 'r': # remove
         q.dequeue();
      else:
         print("Unknown command!")
      command = input()

   print(print_queue(q.data, q.front, q.back))

if __name__ == "__main__":
   main()