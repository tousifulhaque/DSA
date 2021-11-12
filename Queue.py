import time
from collections import deque


class Queue():
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


order_list = Queue()


def taking_order():
    order_list.enqueue(input())


def delivering_order():
    print(order_list.dequeue())


for i in range(5):
    taking_order()


for i in range(5):
    delivering_order()
