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
    # NOTE: This is the general pattern for accessing any node in a linked
    #       list, we have to start at the head and repeatedly move to the next
    #       node in order to "traverse" the list. Regardless of whether this is
    #       done iteratively or recursively (see below), this takes O(n) time.
    #       Doubling the length of the list also doubles the number of nodes
    #       that must be traversed.
    #
    # Start with a current node being the lst's head.
    # For i from 0 to idx, do:
    #     Set the current node to the current node's next.
    # Return the current node's value.
    pass


def set(lst, idx, value):
    # NOTE: If we instead wish to traverse the list recursively, we have to
    #       remove something from the list in order to create a smaller version
    #       of the same problem. This means we need to recurse not on a list
    #       but on a *node somewhere in the list*.
    #
    # Set the value within the given list's head with the given idx.
    pass


def _set(node, idx, value):
    # NOTE: Lists are not defined recursively -- lists do not contain lists --
    #       but nodes contain nodes. When recursing, we pass the given node's
    #       next, effectively removing the given node from the list, and
    #       decrement the given idx to indicate that we need to traverse one
    #       fewer node in the future.
    #
    # If the given idx is 0, then:
    #     Set the given node's value to the given value.
    # Else, do:
    #     Recurse on the given node's next with the given idx - 1.


def add(lst, idx, value):
    # Create a new node containing the given value.
    #
    # If the given idx is 0, then:
    #     Set the new node's next to the lst's head.
    #     Set the lst's head to the new node.
    # Else, do:
    #     Start with a current node being the lst's head.
    #     For i from 0 to idx - 1, do:
    #         Set the current node to the current node's next.
    #     Set the new node's next to the current node's next.
    #     Set the current node's next to the new node.
    #
    # Increment the lst's size.
    pass


def remove(lst, idx):
    # If the given idx is 0, then:
    #     NOTE: Just as with adding, removing from index 0 is a special case,
    #           because it requires modifying the lst's head reference.
    #
    #     Set the lst's head to the lst's head's next.
    #
    # Else, do:
    #     NOTE: Just as with adding, removing generally requires access to the
    #           previous node, whose next reference will have be modified.
    #
    #     Start with a current node being the lst's head.
    #     For i from 0 to idx - 1, do:
    #         Set the current node to the current node's next.
    #     Set the current node's next to the current node's next's next.
    #
    # Decrement the lst's size.
    pass
