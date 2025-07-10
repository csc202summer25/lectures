class Stack:
    """ A LIFO collection of elements """

    def __init__(self):
        # NOTE: A stack is a special case of a list, a list that can only be
        #       accessed at one terminus. Thus, a stack can be implented based
        #       on either a linked list or an array list.
        #
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
    # NOTE: In a linked list, accessing the head is O(1), whereas accessing the
    #       tail is O(n), so the head ought to be the top-of-stack.
    #
    # Create a new node containing the given value.
    # Set the new node's next to the stack's head.
    # Set the stack's head to the new node.
    # Increment the stack's size.
    #
    #                   OR
    #
    # NOTE: In an array list, accessing index 0 is O(n), whereas accessing
    #       index n - 1 is O(1), so index n - 1 ought to be the top-of-stack.
    #
    # If the stack's size is equal to the stack's capacity, then:
    #     Set the stack's capacity to the stack's capacity * 2.
    #     Create a new array of the stack's capacity.
    #     For i from 0 to the stack's size, do:
    #         Set the new array at i to the stack's array at i.
    #     Set the stack's array to the new array.
    #
    # Set the stack's array at the stack's size to the given value.
    # Increment the stack's size.
    pass


def pop(stack):
    # Set the stack's head to the stack's head's next.
    # Decrement the stack's size.
    #
    #                   OR
    #
    # Decrement the stack's size.
    pass


def peek(stack):
    # Return the stack's head's value.
    #
    #                   OR
    #
    # Return the stack's array at the stack's size - 1.
    pass
