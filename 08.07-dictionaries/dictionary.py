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
    # NOTE: Every operation will involve hashing the given key in order to
    #       transform it into an integer, which we can then use to index an
    #       array in O(1) time. This is the only operation that we can
    #       generally perform in better than a BST's O(log n) time.
    #
    # Hash the given key and mod it by the capacity.
    # Start with a current node being the value at that hash code.
    #
    # NOTE: Essentially, a separate chaining hash table is a collection of
    #       linked lists that uses a hash function to quickly eliminate lists
    #       that cannot possibly contain the desired key-value pair. Any lists
    #       at other hash codes need not be searched.
    #
    # While the current node's key is not the given key, do:
    #     Set the current node to the current node's next.
    #
    # Return the current node's value.
    pass


def insert(dct, key, value):
    # NOTE: Generally, designing a perfect hash function is more trouble than
    #       it's worth. Since collisions are inevitable, we must instead place
    #       each key-value pair into a linked list node, so that in the future
    #       we can append any colliding pairs instead of overwriting existing.
    #
    # Hash the given key and mod it by the capacity.
    #
    # If the value in the array at that hash code is None, then:
    #     Create a new node containing the given key-value pair.
    #     Set the new node's next to None.
    #     Set the value in the array at that hash code to the new node.
    #     Increment the size.
    # Else, do:
    #     Start with a current node being the value at that hash code.
    #     While the current node's key is not the given key, do:
    #         If the current node's next is None, then:
    #             Create a new node containing the given key-value pair.
    #             Set the new node's next to None.
    #             Set the current node's next to the new node.
    #             Increment the size.
    #         Set the current node to the current node's next.
    #
    #     NOTE: The only way to break out of the above loop is for the current
    #           node to contain the given key, whether that's a node that was
    #           already in the dictionary or a node that we just created.
    #
    #     Set the current node's value to the given value.
    pass


def remove(dct, key):
    # NOTE: Unlike an array list, a hash table's keys may be scattered around
    #       the array, so we cannot rely on a range of indices to tell us
    #       which array elements are actually in the dictionary; we have to
    #       reset them back to None when they are removed.
    #
    # Hash the given key and mod it by the capacity.
    # Set the value in the array at that hash code to None.
    # Decrement the size.
    #
    # TODO: The above assumes no collisions. Update it to remove the given key
    #       from the appropriate separate chaining linked list.
    pass


def keys(dct):
    pass
