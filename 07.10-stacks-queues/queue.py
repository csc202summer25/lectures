class Queue:
    """ A FIFO collection of elements """

    def __init__(self):
        # The head of the backing linked list:
        self.head = None
        # The tail of the backing linked list:
        self.tail = None
        # The number of elements in this queue:
        self.size = 0
        #
        #                 OR
        #
        # The length of the backing array:
        self.capacity = 4
        # The backing array:
        self.array = [None] * self.capacity
        # The index of the front of the queue:
        self.front = -1
        # The index of the back of the queue:
        self.back = -1


class Node:
    """ A single node in a linked list """

    def __init__(self, value, next):
        # The value contained in this node:
        self.value = value
        # The next node in the linked list:
        self.next = next


def enqueue(queue, value):
    pass


def dequeue(queue):
    pass


def peek(queue):
    pass
