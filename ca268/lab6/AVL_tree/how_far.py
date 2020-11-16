from Node import Node

#
#   Function to add an item to a tree.
#
#   This is not good object oriented coding. It's not even very polite. It directly interferes with the tree's innards.
#
def add(tree, item):
    """ Add this item to its correct position on the tree """
    # This is a non recursive add method. A recursive method would be cleaner.
    if tree.root == None: # ... Empty tree ...
        tree.root = Node(item, None, None) # ... so, make this the root
    else:
        # Find where to put the item
        parent_stack = []
        child_tree = tree.root
        while child_tree != None:
            parent_stack.append(child_tree)
            if item < child_tree.item: # If smaller ... 
                child_tree = child_tree.left # ... move to the left
            elif item > child_tree.item:
                child_tree = child_tree.right

        # child_tree should be pointing to the new node, but we've gone too far
        # we need to modify the parent nodes
        parent = parent_stack[-1]
        node = Node(item, None, None)
        if item < parent.item:
            parent.left = node
        elif item > parent.item:
            parent.right = node
        else:
            return
        # Ignore the case where the item is equal.
        
    #
    #   Note that you can get the height of a node by calling tree.recurse_height().
    #       For example, the height of the root is tree.recurse_height(tree.root)
    #
    while node != None:
        if abs(tree.recurse_height(node.left) - tree.recurse_height(node.right)) > 1:
            # Found an out of order node.
            unbalanced_node_item = node.item
            # print("unbalanced_node_item:", unbalanced_node_item)
            top = node
            mid = top.left if item < top.item else top.right
            bot = mid.left if item < mid.item else mid.right

            # Work out which rotation is necessary (which one is in the middle)
            if top.item < mid.item < bot.item:  # rr case
                new_top = mid
                top_right = mid.left
                mid.left = top
            elif bot.item < mid.item < top.item:  # ll case
                new_top = mid
                top.left= mid.right
                mid.right = top
            elif mid.item < bot.item < top.item:  # lr case
                new_top = bot
                mid.right = bot.left
                top.left = bot.right
                bot.left = mid
                bot.right = top
            else:  # top.item < bot.item < mid.item rl case
                new_top = bot
                mid.left = bot.right
                top.right = bot.left
                bot.left = top
                bot.right = mid

            # make the parent the top point point to new top
            top_parent = None if len(parent_stack) == 0 else parent_stack.pop()
            if top_parent is None:
                tree.root = new_top
            elif top.item < top_parent.item:
                top_parent.left = new_top
            else:
                top_parent.right = new_top
            
            return unbalanced_node_item
    
        node = None if len(parent_stack) == 0 else parent_stack.pop()

    
