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

    def count(self):
        if self.head is not None:
            count = 0
            ptr = self.head
            while ptr is not None:
                count += 1
                ptr = ptr.next

            return count

    def after(self, item):
        if self.head is not None:
            ptr = self.head
            while ptr.item != item and ptr is not None:
                ptr = ptr.next

            if ptr.next is not None:
                return ptr.next.item



def main():  # for testing
    ll = LinkedList()
    ll.add(1)
    ll.add(6)
    ll.add(2)
    print('after {} is'.format(ll.head.item), ll.after(ll.head.item))


if __name__ == '__main__':
    main()