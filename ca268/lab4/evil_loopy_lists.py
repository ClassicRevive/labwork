#!/usr/bin/env python3

class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

# Note, these functions are called methods "A method is a function that is stored as a class attribute"
class LinkedList:
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


def detect_loop(ll):
    if not(ll.is_empty()):  # search list for link to head
        ptr = ll.head
        while ptr is not None:
            if ptr.next is ll.head:  # if next refers to head object, not item!
                return True
            ptr = ptr.next
        return False
    else:
        return False
