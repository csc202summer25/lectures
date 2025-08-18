class Dictionary:
    """ A collection of key-value pairs """

    def __init__(self):
        # The length of the backing array:
        self.capacity = 5
        # The backing array:
        self.array = [None] * self.capacity
        # The number of pairs in this dictionary:
        self.size = 0


class Node:
    """ A single node in a linked list """

    def __init__(self, key, value, next):
        # The key contained in this node:
        self.key = key
        # The value contained in this node:
        self.value = value
        # The next node in the linked list:
        self.next = next


def get(dct, key):
    # Hash the given key and mod it by the capacity.
    # Start with a current node being the value at that hash code.
    #
    # While the current node's key is not the given key, do:
    #     Set the current node to the current node's next.
    #
    # Return the current node's value.
    pass


def insert(dct, key, value):
    # Hash the given key and mod it by the capacity.
    #
    # If the value in the array at that hash code is None, then:
    #     Create a new node containing the given key-value pair.
    #     Set the new node's next to None.
    #     Set the value in the array at that hash code to the new node.
    #     Increment the size.
    # Else, do:
    #     Start with a current node being the value at that hash code.
    #
    #     While the current node's key is not the given key, do:
    #         If the current node's next is None, then:
    #             Create a new node containing the given key-value pair.
    #             Set the new node's next to None.
    #             Set the current node's next to the new node.
    #             Increment the size.
    #         Set the current node to the current node's next.
    #
    #     Set the current node's value to the given value.
    pass


def remove(dct, key):
    # TODO: This assumes no collisions; update to remove from the appropriate
    #       separate chaining linked list.
    #
    # Hash the given key and mod it by the capacity.
    # Set the value in the array at that hash code to None.
    # Decrement the size.
    pass


def keys(dct):
    pass
