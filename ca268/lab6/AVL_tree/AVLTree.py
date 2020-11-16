#
#   AVL tree. The add method contains an AVL fix section which restructures the tree
#               if it is unbalanced.
#           There is no delete method.
#
#           Also, you should note that this is an educational example. A real world implementation would
#           not find the height as shown, instead each node would store balance information so that it
#           could be looked up rather than discovered.
#           Note that finding the height as done here is an O(n) operation.
#           Maintaining and updating the balance is an O(1) operation.
#

from Node import Node

class AVLTree:
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
            parent_stack = [] # Use a list as a stack to hold parents
            child_tree = self.root
            while child_tree != None:
                parent_stack.append(child_tree) # remember the parent for the path back (when checking for AVLness).
                if item < child_tree.item: # If smaller ... 
                    child_tree = child_tree.left # ... move to the left
                else:
                    child_tree = child_tree.right

            # child_tree is pointing to the new node, but we've gone too far
            # we need to get to the parent to change its pointer
            parent = parent_stack[-1]       # The parent is the last item on the parent stack
            node = Node(item, None, None)
            if item < parent.item: # left?
                parent.left = node
            elif item > parent.item: # right?
                parent.right = node
            else:
                # Else this item is already in the tree and so not added
                return

            # The item has been added, now see if we are AVL unbalanced - go back up the tree.
            while node != None:
                if abs(self.recurse_height(node.left) - self.recurse_height(node.right)) > 1:
                    # Found an out of order node! Need to fix
                    # First get the three nodes to restructure
                    top = node
                    mid = top.left if item < top.item else top.right
                    bot = mid.left if item < mid.item else mid.right

                    # Work out which rotation we need to do. (which one is in the middle)
                    if top.item < mid.item < bot.item:
                        # mid in the middle => put on top
                        new_top = mid
                        top.right = mid.left
                        mid.left = top
                    elif bot.item < mid.item < top.item:
                        # Right rotation
                        new_top = mid
                        top.left = mid.right
                        mid.right = top
                    elif mid.item < bot.item < top.item:
                        # double 1
                        new_top = bot
                        mid.right = bot.left
                        top.left = bot.right
                        bot.left = mid
                        bot.right = top
                    else:# top.item < bot.item < mid.item:
                        # double 2
                        new_top = bot
                        mid.left = bot.right
                        top.right = bot.left
                        bot.left = top
                        bot.right = mid

                    # Make the parent of top point to the new top
                    top_parent = None if len(parent_stack) == 0 else parent_stack.pop()
                    if top_parent == None:
                        self.root = new_top
                    elif top.item < top_parent.item:
                        top_parent.left = new_top
                    else:
                        top_parent.right = new_top
                    break

                # Carry on up the path be getting the parent from the stack (which was built on the way down)
                node = None if len(parent_stack) == 0 else parent_stack.pop()

    def recursive_contains(self, item, ptr):
        """ returns a pointer to the node rather than a boolean, None if not present """
        if ptr == None:
            return None
        else:
            if item == ptr.item:
                return ptr
            elif item < ptr.item:
                return self.recursive_contains(item, ptr.left)
            else:
                return self.recursive_contains(item, ptr.right)

    def contains(self, item):
        """ returns a pointer to the node rather than a boolean, None if not present """
        return self.recursive_contains(item, self.root)

    def recurse_height(self, ptr):
        if ptr == None:
            return 0
        else:
            return 1 + max(self.recurse_height(ptr.left), self.recurse_height(ptr.right))

    def height(self): return self.recurse_height(self.root)

    def recurse_str(self, ptr):
        if ptr == None:
            return ""
        else:
            return self.recurse_str(ptr.left) + str(ptr.item) + "," + self.recurse_str(ptr.right)
            
    def __str__(self):
        return self.recurse_str(self.root)

#
#   BST is only required for testing.
#
from BST import BST

def main():
    """ Testing the AVL tree against the BST tree for various data. """
    sample_trees = [
                [],     # Empty
                [10],   # One element
                [10, 20, 30, 40, 50, 60],   # left leaning
                [60, 50, 40, 30, 20, 10],   # right leaning
                [5, 7, 10],   
                [10, 7, 5],
                [10, 5, 7],   # Double rotation 
                [5, 10, 7],   # Double rotation (other direction)
                [40, 20, 10, 30, 60, 50, 70],   # balanced
                [40, 20, 10, 30, 60, 50, 70, 5],   # balanced one leftmost leaf
                [40, 20, 10, 30, 60, 50, 70, 75, 80],   # not AVL (75 80 put over the edge)
                [40, 20, 10, 30, 60, 50, 70, 5, 4],     # not AVL (5 4 put over the edge)
                ]


    for lst in sample_trees[:]:
        bst = BST()
        avl = AVLTree()

        # Add lst contents to the tree
        for num in lst:
            bst.add(num)
            avl.add(num)

        print("BST: " + str(bst) + " [" + str(bst.height()) + "]")
        print("AVL: " + str(avl) + " [" + str(avl.height()) + "]")

if __name__ == "__main__":
    main()

""" Output
BST:  [0]
AVL:  [0]
BST: 10, [1]
AVL: 10, [1]
BST: 10,20,30,40,50,60, [6]     # Note that the BST and the AVL tree have the same data
AVL: 10,20,30,40,50,60, [3]     # but the AVL tree has a height of 3. The height of the AVL tree will be O(log(N))
BST: 10,20,30,40,50,60, [6]     # Whereas the BST will have a worst case height of O(N).
AVL: 10,20,30,40,50,60, [3]
BST: 5,7,10, [3]
AVL: 5,7,10, [2]
BST: 5,7,10, [3]
AVL: 5,7,10, [2]
BST: 5,7,10, [3]
AVL: 5,7,10, [2]
BST: 5,7,10, [3]
AVL: 5,7,10, [2]
BST: 10,20,30,40,50,60,70, [3]
AVL: 10,20,30,40,50,60,70, [3]
BST: 5,10,20,30,40,50,60,70, [4]
AVL: 5,10,20,30,40,50,60,70, [4]
BST: 10,20,30,40,50,60,70,75,80, [5]
AVL: 10,20,30,40,50,60,70,75,80, [4]
BST: 4,5,10,20,30,40,50,60,70, [5]
AVL: 4,5,10,20,30,40,50,60,70, [4]

"""
