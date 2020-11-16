#
#  This linked list use built-ins: str(), iter(), len(), in()
#
#   These functions are implemented using recursion (except iter)
#
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

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

    def __iter__(self):
        cursor = self.head
        while cursor is not None:
            yield cursor.item
            cursor = cursor.next

    def recursive_len(self, ptr):
        if ptr == None:
            return 0
        else:
            return 1 + self.recursive_len(ptr.next)

    def __len__(self):
        return self.recursive_len(self.head)

    def recursive_contains(self, ptr, item):
        if ptr == None:
            return False
        else:
            return item == ptr.item or self.recursive_contains(ptr.next)

    def __in__(self, item):
        return recursive_contains(self.head, item)

    def recursive_str(self, ptr):
        if ptr == None:
            return ""
        else:
            return str(ptr.item) + "->" + self.recursive_str(ptr.next)

    def __str__(self):
        return self.recursive_str(self.head)


class HashSet:
    def __init__(self, capacity=10):
        # Create a list to use as the hash table
        self.table = [None] * capacity

    def add(self, item):
        # Find the hash code
        h = hash(item)
        index = h % len(self.table)

        # Check is it empty
        if self.table[index] == None:
            self.table[index] = LinkedList() # Need a new linked list for this entry
            self.table[index].add(item)
            return None

        if item not in self.table[index]:  # Collision detected
            # Only add it if not already there (this is a set)
            self.table[index].add(item)

        return (index, item)

    def average_bucket_length(self):
        total = 0
        num = 0
        for i in self.table:
            if i is not None:
                total += len(i)
                num += 1
        return total / num

    def min_max_bucket_length(self):
        # create a list of lengths of buckets, get min and max
        bucket_lengths = []

        for i in self.table:
            if i is not None:
                bucket_lengths.append(len(i))

        return (min(bucket_lengths), max(bucket_lengths))

    def __iter__(self):
        i = 0
        cursor = self.table[i]
        while i < len(self.table):  # could have used a "for" loop
            if self.table[i] is not None:
                for j in self.table[i]:
                    yield j

            i += 1
                