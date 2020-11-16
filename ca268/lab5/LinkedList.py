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

    def recurse_even(self, ptr):
        if ptr is None:  # base case
            return 0
        elif ptr.item % 2 == 0:  # even case
            return 1 + self.recurse_even(ptr.next)
        else:  # odd case
            return self.recurse_even(ptr.next)

    def count_even(self):
        return self.recurse_even(self.head)


    def recurse_present(self, ptr, item):
        if ptr is None:  # base case (failure)
            return False
        elif ptr.item == item:
            return True  # success case
        else:
            return self.recurse_present(ptr.next, item)  # recursive case

    def is_present(self, item):
        return self.recurse_present(self.head, item)

    def recurse_max(self, ptr, largest):
        if ptr is None:  # base case
            return largest
        elif largest < ptr.item:  # "new max" case
            largest = ptr.item

        return self.recurse_max(ptr.next, largest)  # recursive case

    def largest(self):
        return self.recurse_max(self.head, self.head.item)

    def recurse_duplicates(self, ptr):
        if ptr is None or ptr.next is None:  # base case
            return False
        elif ptr.item == ptr.next.item:  # success case
            return True
        else:
            return self.recurse_duplicates(ptr.next)

    def duplicates(self):
        return self.recurse_duplicates(self.head)


def main():
    import sys

    # Read each set
    line = sys.stdin.readline()
    items = line.strip().split()
    
    ll = LinkedList()
    bool = str(ll.duplicates())[0]
    print(bool, end="")  # Only print the first letter of the result (F for false, T for true)
    for item in items:
        ll.add(item)
        bool = str(ll.duplicates())[0] # Only print the first letter of the result
        print(bool, end="")
        
    print()

if __name__ == '__main__':
    main()