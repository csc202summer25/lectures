class SortedList:
    """ A sorted collection of elements """

    def __init__(self):
        # The length of the backing array:
        self.capacity = 4
        # The backing array:
        self.array = [None] * self.capacity
        # The number of elements in this sorted list:
        self.size = 0


def insert(lst, value):
    # If the lst's size is equal to the lst's capacity, then:
    #     Set the lst's capacity to the lst's capacity * 2.
    #     Create a new array of the lst's capacity.
    #     For i from 0 to the lst's size, do:
    #         Set the new array at i to the lst's array at i.
    #     Set the lst's array to the new array.
    #
    # Start with i being the lst's size.
    # While the array at i - 1 is in-bounds, greater than the given value, do:
    #     Set the array at i to the array at i - 1.
    #     Decrement i.
    #
    # Set the array at i to the given value.
    # Increment the size.
    pass


def remove(lst, idx):
    # For i from the given idx to the lst's size - 1, do:
    #     Set the array at i to the array at i + 1.
    #
    # Decrement the size.
    pass


def find(lst, value):
    # Start with low being 0 and high being the lst's size - 1.
    #
    # While low is less than or equal to high, do:
    #     Set mid to the floor of (low + high) / 2.
    #     If the array at mid is equal to the given value, then:
    #         Return mid.
    #     Else if the array at mid is less than the given value, then:
    #         Set low to mid + 1.
    #     Else, do:
    #         Set high to mid - 1.
    #
    # (the value is not in the list)
    pass


def create(array, size):
    # NOTE: In the worst case, each of the n insertions takes O(n) time; this
    #       is thus O(n^2). This is not the best possible way to sort a list,
    #       but it is practically trivial to implement given the above insert
    #       function.
    #
    # Create a new sorted list.
    # For i from 0 to the given size, do:
    #     Insert the given array at the given size into the sorted list.
    # Return the sorted list.
    pass
