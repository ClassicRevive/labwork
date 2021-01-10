#
#  Just a class to store the item and the next pointer
#
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

    def length(self):
        if self.head is not None:
            ptr = self.head
            count = 0
            while ptr is not None:
                count += 1
                ptr = ptr.next

            return count
        else:
            return 0

def findmax(ll):
    if ll.head is not None:
        curr_max = ll.head.item
        ptr = ll.head
        while ptr is not None:
            if ptr.item > curr_max:
                curr_max = ptr.item
            ptr = ptr.next

        return curr_max


def main():  # testing
    ll = LinkedList()
    ll.add(1)
    ll.add(5)
    ll.add(4)
    print('length', ll.length())
    print('max', str(findmax(ll)))


if __name__ == '__main__':
    main()