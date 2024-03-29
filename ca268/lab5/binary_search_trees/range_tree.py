class Node:
    """ A node in a BST. It may have left and right subtrees """
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    """ An implementation of a Binary Search Tree """
    def __init__(self):
        self.root = None

    def add(self, item):
        """ Add this item to its correct position on the tree """
        # This is a non recursive add method.
        if self.root == None: # ... Empty tree ...
            self.root = Node(item, None, None) # ... so, make this the root
        else:
            # Find where to put the item
            child_tree = self.root
            while child_tree != None:
                parent = child_tree
                if item < child_tree.item: # If smaller ... 
                    child_tree = child_tree.left # ... move to the left
                else:
                    child_tree = child_tree.right

            # child_tree should be pointing to the new node, but we've gone too far
            # we need to modify the parent nodes
            if item < parent.item:
                parent.left = Node(item, None, None)
            elif item > parent.item:
                parent.right = Node(item, None, None)
            #else:
            #   equal ... don't add it to the set.
    
    def recursive_count(self, ptr, hi, lo):
        if ptr is None:
            return 0
        elif lo <= ptr.item <= hi:  # success case
            return 1 + sum([self.recursive_count(ptr.left, hi, lo), 
                           self.recursive_count(ptr.right, hi, lo)])
        elif lo < ptr.item:  # "check lower" case
            return self.recursive_count(ptr.left, hi, lo)
        else:  # "check higher" case
            return self.recursive_count(ptr.right, hi, lo)


    def count(self, lo, hi):
        return self.recursive_count(self.root, hi, lo)


def main():
    bst = BST()
    bst.add(4)
    bst.add(2)
    bst.add(5)
    bst.add(1)
    print(bst.count(4, 5))


if __name__ == '__main__':
    main()