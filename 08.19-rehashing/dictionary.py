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
    # NOTE: Once the load factor would exceed 1 (once the size is equal to the
    #       capacity prior to insertion), at least one collision is inevitable,
    #       and the hash table must be rehashed. Ideally, the capacity would
    #       remain prime, but doubling and adding one is a good approximation.
    #
    # If the size is equal to the capacity, then:
    #     Set the capacity to the capacity * 2 + 1.
    #     Create a new array of that capacity.
    #
    #     NOTE: Rehashing a hash table is not as simple as copying all of the
    #           existing key-value pairs into a new array, because their hash
    #           codes may have changed now that the capacity has changed. It is
    #           generally possible that two existing keys collide under the new
    #           capacity, however, it is not possible to encounter two of the
    #           same key when rehashing, so colliding keys can be prepended
    #           without searching the corresponding linked list.
    #
    #     For i from 0 to the old capacity, do:
    #         Start with a current node being the value in the array at i.
    #         While the current node is not None, do:
    #             Hash the current node's key and mod it by the new capacity.
    #             Set a temp node to the current node's next.
    #             Set the current node's next to the value in the new array at
    #              that new hash code.
    #             Set the new array at that new hash code to the current node.
    #             Set the current node to the temp node.
    #
    #     Set the dictionary's array to the new array.
    #
    # NOTE: The hash code is computed based on the capacity, so if rehashing is
    #       required, that must be done before computing the hash code.
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
    # Hash the given key and mod it by the capacity.
    #
    # If the value in the array at that hash code contains the given key, then:
    #     Set the value in the array at that hash code to its next.
    # Else, do:
    #     Start with a current node being the value in the array at that code.
    #     While the current node's next's key is not the given key, do:
    #         Set the current node to the current node's next.
    #     Set the current node's next to the current node's next's next.
    #
    # Decrement the size.
    pass


def keys(dct):
    # TODO: Iterate over all of the key-value pairs, in the same manner as when
    #       rehashing, and collect them all into a list.
    pass
