class Queue:
    """ A FIFO collection of elements """

    def __init__(self):
        # The length of the backing array:
        self.capacity = 4
        # The backing array:
        self.array = [None] * self.capacity
        # The index of the front of the queue:
        self.front = -1
        # The index of the back of the queue:
        self.back = -1


def enqueue(queue, value):
    pass


def dequeue(queue):
    pass


def peek(queue):
    pass
