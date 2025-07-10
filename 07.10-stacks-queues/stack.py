class Stack:
    """ A LIFO collection of elements """

    def __init__(self):
        # The head of the backing linked list:
        self.head = None
        # The number of elements in this stack:
        self.size = 0
        #
        #                 OR
        #
        # The length of the backing array:
        self.capacity = 4
        # The backing array:
        self.array = [None] * self.capacity
        # The number of elements in this stack:
        self.size = 0


class Node:
    """ A single node in a linked list """

    def __init__(self, value, next):
        # The value contained in this node:
        self.value = value
        # The next node in the linked list:
        self.next = next


class Stack:
    """ A LIFO collection of elements """

    def __init__(self):


def push(stack, value):
    pass


def pop(stack):
    pass


def peek(stack):
    pass
