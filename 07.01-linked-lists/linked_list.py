class List:
    """ An ordered collection of elements """

    def __init__(self):
        # The head of the backing linked list:
        self.head = None
        # The number of elements in this list:
        self.size = 0


class Node:
    """ A single node in a linked list """

    def __init__(self, value, next):
        # The value contained in this node:
        self.value = value
        # The next node in the linked list:
        self.next = next


def get(lst, idx):
    pass


def set(lst, idx, value):
    pass


def add(lst, idx, value):
    # Create a new node containing the given value.
    # Set the new node's next to None.
    #
    # If the given idx is 0, then:
    #     NOTE: Adding to index 0 is a special case, because it is the only
    #           scenario in which we need to change the list's head.
    #
    #     Set the node's next to the lst's head.
    #     Set the lst's head to the new node.
    #
    # Else, do:
    #     NOTE: By definition, every node contains a reference to the next node
    #           in the list, which means adding a new node generally requires
    #           first finding the *previous* node in the list. The basic
    #           pattern for finding any node in a linked list involves starting
    #           at the head and repeatedly moving to the next node.
    #
    #     Start with a tmp node being the lst's head.
    #     For i from 0 to idx - 1, do:
    #         Set the tmp node to the tmp node's next.
    #     Set the new node's next to the tmp node's next.
    #     Set the tmp node's next to the new node.
    #
    # Increment the lst's size.
    pass


def remove(lst, idx):
    pass
