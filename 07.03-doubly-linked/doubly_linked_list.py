class List:
    """ An ordered collection of elements """

    def __init__(self):
        # The head of the backing linked list:
        self.head = None
        # The tail of the backing linked list:
        self.tail = None
        # The number of elements in this list:
        self.size = 0


class Node:
    """ A single node in a linked list """

    def __init__(self, value, previous, next):
        # The value contained in this node:
        self.value = value
        # The previous node in the linked list:
        self.prev = prev
        # The next node in the linked list:
        self.next = next


def get(lst, idx):
    # NOTE: With a doubly linked list, we don't necessarily have to traverse
    #       the nodes going "forwards" from the head; we could alternatively
    #       go "backwards" from the tail...
    #
    # If the given idx is less than the given lst's size / 2, then:
    #     Start with a current node being the lst's head.
    #     For i from 0 to idx, do:
    #         Set the current node to the current node's next.
    # Else, do:
    #     Start with a current node being the lst's tail.
    #     For i from n to idx, do:
    #         Set the current node to the current node's previous.
    #
    # NOTE: ...this seems clever; unfortunately, getting the middle of the list
    #       still requires traversing roughly n / 2 nodes, and n / 2 is still
    #       O(n). We still cannot support fast "random access".
    #
    # Return the current node's value.
    pass


def set(lst, idx, value):
    pass


def add(lst, idx, value):
    pass


def remove(lst, idx):
    pass
