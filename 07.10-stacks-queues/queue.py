class Queue:
    """ A FIFO collection of elements """

    def __init__(self):
        # The head of the backing linked list:
        self.head = None
        # The tail of the backing linked list:
        self.tail = None
        # The number of elements in this queue:
        self.size = 0


class Node:
    """ A single node in a linked list """

    def __init__(self, value, next):
        # The value contained in this node:
        self.value = value
        # The next node in the linked list:
        self.next = next


def enqueue(queue, value):
    # NOTE: Adding to the head or to the tail is O(1), so strictly speaking it
    #       doesn't matter which is the back of the queue...
    #
    # Create a new node containing the given value.
    # Set the new node's next to None.
    #
    # If the queue's size is 0, then:
    #     Set the queue's head to the new node.
    # Else, do:
    #     Set the tail's next to the new node.
    #
    # Set the tail to the new node.
    # Increment the queue's size.
    pass


def dequeue(queue):
    # NOTE: ...but removing from the head is O(1) whereas removing from the
    #       tail is O(n). The head is the front, thus, the tail is the back.
    #
    # Set the queue's head to the queue's head's next.
    #
    # If the queue's size is 1, then:
    #     Set the queue's tail to None.
    #
    # Decrement the queue's size.
    pass


def peek(queue):
    # Return the queue's head's value.
    pass
