from collections import deque
import time, threading

""" Naive Solution where only one consumer is being served at one time """

class Queue:
    
    """ Simple implementation of a Quque using the collections.qequeue object """

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):

        if len(self.buffer)==0:
            return None
        else:
            return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)

food_order_queue = Queue()

""" Create the main event loop where the producer creates an order and consumer takes the latest order and processes it """

def place_order(orders):

    for order in orders:

        time.sleep(0.5)
        print(f'Creating a {order} Order..')
        food_order_queue.enqueue(order)

def serve_order():

    time.sleep(1)

    while True:

        if food_order_queue.is_empty():
            break

        order = food_order_queue.dequeue()
        print(f'Serving Order {order}')
        food_order_queue.dequeue()
        time.sleep(2)


if __name__ == '__main__':

    orders = ['pizza','samosa','pasta','biryani','burger']

    t1 = threading.Thread(target=place_order, args=(orders,))
    t1.setName('Producer Thread')
    
    t2 = threading.Thread(target=serve_order)
    t2.setName('Consumer Thread')
    t1.start()
    t2.start()

    print(threading.activeCount())
    

    



