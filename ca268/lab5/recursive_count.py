#!/usr/bin/env python3

class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class LinkedLList:
    def __init__(self):
        self.head = None

    def add(self, item):
        self.head = Node(item, self.head)

    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next    # remove the item by moving the head pointer
            return item

    def is_empty(self):
        return self.head == None

    def recurse_count(self, ptr):
        if ptr == None:
            return 0
        else:
            return 1 + self.recurse_count(ptr.next)
    
    def count(self):
        return self.recurse_count(self.head) 
