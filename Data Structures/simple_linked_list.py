class Node:
    def __init__(self, value):

        self.next = None
        self.value = value


class LinkedList:
    def __init__(self, value):

        self.head = Node(value)

    def print_nodes(self):

        current_node = self.head

        while current_node:

            print(current_node.value)
            current_node = current_node.next

    def append(self, value):

        current_node = self.head

        # check that the next node has a node otherwise stay on current node

        while current_node.next:
            current_node = current_node.next

        current_node.next = Node(value)

    def prepend(self, value):

        # look for a given value and insert before that value

        current_node = self.head

        if self.head is None:
            self.head = Node(value)

        newNode = Node(value)

        prevNode = self.head
        self.head = newNode
        self.head.next = prevNode

    def get_index(self, index):

        current_node = self.head

        counter = 0

        while counter != index:

            current_node = current_node.next
            counter += 1

        return current_node

    def insert(self, index, value):

        current_node = self.head

        if self.head is None:
            self.head = Node(value)

        original = self.get_index(index)

        leader_node = self.get_index(index - 1)

        print("this index node, ", index, "is", leader_node.value)

        after_node = leader_node.next

        leader_node.next = Node(value)

        self.print_nodes()


def count_nodes(head):

    counter = 1
    current = head

    while current.next is not None:
        current = current.next
        counter += 1

    return counter


def is_head(node):
    if node.prev is None:
        return True
    return False


a = Node(6)
b = Node(3)
c = Node(4)
d = Node(2)
e = Node(1)

a.next = b

b.next = c
b.prev = a

c.next = d
d.next = e

l = LinkedList(123)
l.append(12)
l.insert(1, 10)
