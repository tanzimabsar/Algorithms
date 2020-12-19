class Node:
    def __init__(self, value):

        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, value):

        self.root = Node(value)


def dfs_in_order(root, list):

    list.append(root.value)

    if root.left:
        dfs_in_order(root.left, list)

    if root.right is not None:
        dfs_in_order(root.right, list)

    return list


def solution(root):
    def isSymmetric(root) -> bool:
        return ismirror(root, root)

    def ismirror(t1, t2):

        # this is our base case, check if both nodes are null
        if t1 is None and t2 is None:
            return True

        # check if either node is none -- not symmetric
        elif t1 is None or t2 is None:
            return False
        return (
            (t1.value == t2.value)
            and ismirror(t1.right, t2.left)
            and ismirror(t1.left, t2.right)
        )

    return isSymmetric(root)


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(2)
tree.root.right.right = Node(3)
tree.root.right.left = Node(4)
tree.root.left.right = Node(4)
tree.root.left.left = Node(3)

print(dfs_in_order(tree.root, []))
print(solution(tree.root))
