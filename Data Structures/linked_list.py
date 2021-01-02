# Implementation of a linked list in Python 3.8


class Node:
    def __init__(self, data=None, next_node=None):

        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count


myList = LinkedList()
myList.insert(1)
myList.insert(5)
myList.insert(4)
myList.insert(3)


print(myList.size())
