class BinarySearchTreeNode:
    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):

        if data == self.data:
            return

        # left has lower items and right has higher items

        # if it is less than the curent node then add it to the left

        if data < self.data:

            if self.left:
                self.left.add_child(data)

            # if there is nothing in the right node then create a new node

            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)

            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        # visit the base node
        elements.append(self.data)

        # visit the right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements


def build_tree(elements):

    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == "__main__":

    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    tree = build_tree(numbers)
    print(tree.in_order_traversal())
    print(tree)
