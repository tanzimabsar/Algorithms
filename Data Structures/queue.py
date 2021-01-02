from collections import deque
import time

""" Naive Solution where only one consumer is being served at one time """


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):

        if len(self.buffer) == 0:
            return None
        else:
            return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


""" Create the main event loop where the producer creates an order and consumer takes the latest order and processes it """


def place_order(orderqueue, item):

    time.sleep(0.5)
    print(f"Creating a {item} Order..")
    orderqueue.enqueue(order)


def serve_order(orderqueue):

    time.sleep(2)
    print(f"Serving Order")
    orderqueue.dequeue()


if __name__ == "__main__":

    orderqueue = Queue()

    orders = ["pizza", "samosa", "pasta", "biryani", "burger"]

    for order in orders:
        place_order(orderqueue, order)
        time.sleep(1)
        serve_order(orderqueue)
