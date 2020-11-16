def str_hash(s):
        """ Return a normal hash, unless it is a string. """
        if not isinstance(s, str):
            return hash(s) # not a string => use the normal hash function
        else:
            # just use the sum of hash of each character in the string
            h = 0
            n = len(s)
            # Java String hash method
            for i in range(n):
                h = h + ord(s[i])*31**(n-(i + 1))

            return h

class HashSet:
    def __init__(self, capacity=10):
        # Create a list to use as the hash table
        self.table = [None] * capacity
        

    def add(self, item):
        # Find the hash code
        h = str_hash(item)
        index = h % len(self.table)

        # Check is it empty
        if self.table[index] == None:
            self.table[index] = LinkedList() # Need a new linked list for this entry

        if item not in self.table[index]:
            # Only add it if not already there (this is a set)
            self.table[index].add(item)
