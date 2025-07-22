class SortedList:
    """ A sorted collection of elements """

    def __init__(self):
        # NOTE: In order to implement an efficient binary search, this must be
        #       an array list to support fast random access of the element at
        #       the midpoint.
        #
        # The length of the backing array:
        self.capacity = 4
        # The backing array:
        self.array = [None] * self.capacity
        # The number of elements in this sorted list:
        self.size = 0


def insert(lst, value):
    # NOTE: Inserting into a sorted list is just like adding to an array list,
    #       except that we will not allow the user to specify an index at which
    #       to add -- rather, a value must be added at whatever index we
    #       determine will maintain sorted order.
    #
    # If the lst's size is equal to the lst's capacity, then:
    #     Set the lst's capacity to the lst's capacity * 2.
    #     Create a new array of the lst's capacity.
    #     For i from 0 to the lst's size, do:
    #         Set the new array at i to the lst's array at i.
    #     Set the lst's array to the new array.
    #
    # NOTE: Essentially, before we can insert into a sorted list, we have to
    #       search for the appropriate index ourselves. Since we have to do a
    #       linear shift to make space anyways, we might as well do this as a
    #       linear seach at the same time.
    #
    # Start with i being the lst's size.
    # While i is greater than 0 and
    #  the lst's array at i is greater than the given value, do:
    #     Set the lst's array at i to the lst's array at i - 1.
    #     Decrement i.
    #
    # Set the lst's array at i to the given value.
    # Increment the size.
    pass


def remove(lst, idx):
    # NOTE: Since the list is known to be in sorted order, removing is exactly
    #       the same as with array lists. We can only ruin the sorted order of
    #       the list by putting things in the wrong place; we cannot possibly
    #       ruin it by taking things out.
    #
    # For i from the given idx to the lst's size - 1, do:
    #     Set the lst's array at i to the lst's array at i + 1.
    #
    # Decrement the size.
    pass


def find(lst, value):
    # NOTE: Since the list is known to be in sorted order, we can find values
    #       more efficiently by comparing them to the middle element: if, for
    #       example, the middle element is too small, then every element in the
    #       first half of the list must also be too small.
    #
    # Start with low being 0 and high being the lst's size - 1.
    #
    # While low is less than or equal to high, do:
    #     Set mid to the floor of (low + high) / 2.
    #     If the lst at mid is equal to the given value, then:
    #         Return mid.
    #     Else if the lst at mid is less than the given value, then:
    #         Set low to mid + 1.
    #     Else, do:
    #         Set high to mid - 1.
    #
    # NOTE: The only way to break out of the loop is for low to become greater
    #       than high without ever returning, which means that the region of
    #       the list to be searched is now empty and we never found the value
    #       for which we were searching.
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
