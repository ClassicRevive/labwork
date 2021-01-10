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
        if self.head is None:  # empty case
            return 0
        else:  # normal case
            ptr = self.head
            count = 0
            while ptr is not None:
                count += 1
                ptr = ptr.next

            return count


def findmax(ll):
        if ll.head is not None:
            ptr = ll.head
            current = ptr.item  # initialise the maximum as the head item
            while ptr is not None:
                if ptr.item > current:
                    current = ptr.item

                ptr = ptr.next

            return current


def main():  # for testing
    ll = LinkedList()
    ll.add(1)
    ll.add(6)
    ll.add(2)
    print('length', ll.length())
    print('max', findmax(ll))



if __name__ == '__main__':
    main()