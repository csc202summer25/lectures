class List:
    """ An ordered collection of elements """

    def __init__(self):
        # The length of the backing array:
        self.capacity = 4
        # The backing array:
        self.array = [None] * self.capacity
        # The number of elements in this list:
        self.size = 0


def get(lst, idx):
    # NOTE: Since the elements of the list are contained within an array, which
    #       is stored as a contiguous block of memory, we can compute any
    #       random element's address using its index and "jump" directly there.
    #
    # Return the lst's array at the given idx.
    pass


def set(lst, idx, value):
    # Set the lst's array at the given idx to the given value.
    pass


def add(lst, idx, value):
    # NOTE: Since arrays have fixed size, if we reach the capacity, we have to
    #       create a new array and copy the elements over. Since this is slow,
    #       we'll double the capacity to avoid extra copies in the future.
    #
    # If the lst's size is equal to the lst's capacity, then:
    #     Set the lst's capacity to the lst's capacity * 2.
    #     Create a new array of the lst's capacity.
    #
    #     NOTE: Some additions will require an additional O(n) capacity
    #           increase, but most additions, amortized over the lifetime of
    #           the list, will find that there is already enough space.
    #
    #     For i from 0 to the lst's size, do:
    #         Set the new array at i to the lst's array at i.
    #     Set the lst's array to the new array.
    #
    # NOTE: In order to support fast random access, the list indices must be
    #       equivalent to the corresponding array indices, so adding an element
    #       at an index requires "shifting" all succeeding elements "down".
    #
    # For i from the lst's size to the given idx, do:
    #     Set the lst's array at i to the lst's array at i - 1.
    #
    # Set the lst's array at the given idx to the given value.
    # Increment the size.
    pass


def remove(lst, idx):
    # NOTE: Just as adding elements requires shifting elements "down" to keep
    #       the resulting elements in a contiguous block of memory, removing
    #       elements requires shifting all succeeding elements "up".
    #
    # For i from the given idx to the lst's size - 1, do:
    #     Set the lst's array at i to the lst's array at i + 1.
    #
    # Decrement the size.
    pass
