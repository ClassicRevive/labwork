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

    def count(self):
        ptr = self.head
        count = 0
        while ptr != None:
            count += 1
            ptr = ptr.next
        
        return count

    def contains(self, item):
        ptr = self.head
        while ptr is not None and ptr.item != item:
            ptr = ptr.next

        return not(ptr is None)

    def after(self, item):
        if self.contains(item):
            ptr = self.head
            while ptr.item != item:
                ptr = ptr.next
            try:
                return ptr.next.item
            except:
                return
        else:
            return

    def before(self, item):
        if self.contains(item) and self.head.item != item:
            ptr = self.head
            while ptr.next.item != item:
                ptr = ptr.next

            return ptr.item
        else:
            return


def main():
    ll = LinkedList()
    ll.add(5)
    ll.add(6)
    print("There are {} elements in the linked list!".format(ll.count()))
    print("contains 5?", ll.contains(5))
    print("before 5? {}".format(ll.before(5)))

if __name__ == '__main__':
    main()