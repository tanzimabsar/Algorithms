""" Let us create a BST and then between a range (non inclusive low and inclusive high) 
    find the sim of all the nodes between them 
"""

class Node:
    def __init__(self, value):

        self.right = None
        self.left = None
        self.value = value


class BST:
    def __init__(self):

        self.root = None

    def print_nodes(self):

        # Naive way of printing the nodes from left, root, right
        current_node = self.root

        while current_node:

            print(current_node.value)
            current_node = current_node.left

        current_node = self.root

        while current_node:

            print(current_node.value)
            current_node = current_node.right

    def breadth_first_traversal(self):

        current_node = self.root
        order_list = []
        queue = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop()
   
            order_list.append(current_node.value)

            if current_node.left is not None:
                queue.insert(0,current_node.left)

            if current_node.right is not None:
                queue.insert(0,current_node.right)

        return order_list

    def breadth_first_traversal_recursive(self, queue, array):

        if len(queue) == 0 :
            return array
        
        current_node = queue.pop()
        array.append(current_node.value)

        if current_node.left is not None:
            queue.insert(0, current_node.left)

        if current_node.right is not None:
            queue.insert(0,current_node.right)

        return self.breadth_first_traversal_recursive(queue, array)

        

    def lookup(self, value):

        current_node = self.root

        while current_node:

            if current_node.value == value:
                print(current_node.value)
                return current_node
            elif current_node.value < value:
                current_node = current_node.left
            elif current_node.value > value:
                current_node = current_node.right

    def insert(self, value):

        newNode = Node(value)

        if self.root is None:
            self.root = newNode
  
        else:
            currentNode = self.root
            while True:
                if value < currentNode.value:
                    if currentNode.left is None:
                        currentNode.left = newNode
                        return self
    
                    currentNode = currentNode.left

                else: 
                    if currentNode.right is None:
                        currentNode.right = newNode
                        return self

                    currentNode = currentNode.right

    def dfs_in_order(self, node, list):

        if node.left:
            self.dfs_in_order(node.left, list)

        list.append(node.value)

        if node.right is not None:
            self.dfs_in_order(node.right, list)
        
        return list

    def dfs_pre_order(self, node, list):

        list.append(node.value)

        if node.left:
            self.dfs_pre_order(node.left, list)

        if node.right:
            self.dfs_pre_order(node.right, list)
        
        return list

    def dfs_post_order(self, node, list):

        if node.left:
            self.dfs_post_order(node.left, list)

        if node.right:
            self.dfs_post_order(node.right, list)

        list.append(node.value)
        
        return list

def getlowest(node, list, l, r):

    """ Traverse the tree and find the lowest number that is non inclusive to l 
    """

    if node:
        if l <= node.value <= r:
            list.append(node.value)
        if l < node.value:
            getlowest(node.left, list, l, r)
        if node.value < r:
            getlowest(node.right, list, l, r)

    return sum(list)

tree = BST()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)
tree.insert(18)

print(getlowest(tree.root, [], 7, 15))
#print(tree.dfs_in_order(tree.root, []))

