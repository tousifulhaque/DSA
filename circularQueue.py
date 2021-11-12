from collections import deque




class circularQueue():

    def __init__(self, max_len):
        self.max_len = max_len
        self.queue = deque(maxlen=max_len)
        self.head = 0
        self.tail = max_len - 1

    def __len__(self):
        return len(self.queue)

    def insert_element(self, value):
        if len(self.queue) == max_len:
            raise MemoryError("The queue is full")
        else:
            self.queue.append(value)
            self.head +=1
            self.tail +=1

testQueue = circularQueue(10)


