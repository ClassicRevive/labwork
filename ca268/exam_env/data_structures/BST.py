class Node:
    ''' A node in a Binary Search Tree. It may have left and right subtrees '''
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    ''' An implementation of a Binary Search Tree '''
    def __init__(self):
        self.root = None

    def recurse_add(self, ptr, item):
        if ptr is None:  # base case
            return Node(item)
        elif item < ptr.item:  # traverse left
            ptr.left = self.recurse_add(ptr.left, item)
        elif item > ptr.item:  # traverse right
            ptr.right = self.recurse_add(ptr.right, item)
        return ptr  # item is a duplicate

    def add(self, item):
        ''' Add this item to its correct position on the tree '''
        self.root = self.recurse_add(self.root, item)


    def height(self):
        return self.recurse_height(self.root)

    def recurse_height(self, ptr):
        if ptr is None:  # base case
            return 0
        else:
            return 1 + max(self.recurse_height(ptr.left), self.recurse_height(ptr.right))

    def inorder(self):
        return self.recurse_in_order(self.root)

    def recurse_in_order(self, ptr):
        if ptr is not None:
            self.recurse_in_order(ptr.left)
            print(ptr.item)
            self.recurse_in_order(ptr.right)



def main():
    bst = BST()
    bst.add(4)
    bst.add(2)
    bst.add(3)
    bst.add(5)
    print('height:', bst.height())
    print('elements in order;')
    bst.inorder()

if __name__ == '__main__':
    main()