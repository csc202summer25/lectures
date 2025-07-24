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
    # NOTE: The following is a merge sort. There are many, many other ways to
    #       sort, but in the worst case scenario, a merge sort is provably the
    #       best. The number of times we can halve a list is logarithmic, and
    #       merging sorted lists is linear, so this is O(n log n).
    #
    # Sort the given array.
    # Return a new sorted list whose array is the sorted array.
    pass


def _sort(array, size):
    # NOTE: To make the given array smaller, so as to obtain the trivially
    #       sorted sub-arrays of length 1, we will first divide the given array
    #       in half -- this produces a smaller version of the same problem,
    #       which can then be solved recursively.
    #
    # If the given size is less than or equal to 1, then:
    #     Return the given array.
    # Else, do:
    #     (create a new array_a containing the elements in the first half)
    #     (create a new array_b containing the elements in the second half)
    #     (recursively sort array_a and array_b)
    #     Return the result of merging the recursively sorted arrays.


def _merge(array_a, n, array_b, m):
    # Create a new array of capacity n + m.
    # Start with i, j, and k all being 0.
    #
    # While i is less than n or j is less than m, do:
    #     If i is greater than or equal to n, then:
    #         Set the new array at k to array_b at j.
    #         Increment j and k.
    #     Else if j is greater than or equal to m, then:
    #         Set the new array at k to array_a at i.
    #         Increment i and k.
    #     Else if array_a at i is less than array_b at j, then:
    #         Set the new array at k to array_a at i.
    #         Increment i and k.
    #     Else, do:
    #         Set the new array at k to array_b at j.
    #         Increment j and k.
    #
    # NOTE: To break out of the loop, both i and j must be out-of-bounds,
    #       meaning that we have reached the ends of both arrays, meaning that
    #       all of their collective elements have been merged.
    #
    # Return the new array
